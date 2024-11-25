#!/usr/bin/python3
"""Test API Documentation"""
import unittest
from api.v1.app import app
import json
from flasgger import Swagger
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)

class TestDocumentation(unittest.TestCase):
    """Test the API documentation"""

    def setUp(self):
        """Set up test client"""
        self.client = app.test_client()

    def test_documentation_available(self):
        """Test if Swagger documentation is available"""
        response = self.client.get('/apidocs/')
        self.assertEqual(response.status_code, 200)

    def test_documentation_content(self):
        """Test if documentation content is valid"""
        response = self.client.get('/apispec_1.json')
        self.assertEqual(response.status_code, 200)
        spec = json.loads(response.data.decode('utf-8'))
        
        # Verify essential elements
        self.assertIn('swagger', spec)
        self.assertIn('info', spec)
        self.assertIn('paths', spec)

    def test_endpoints_documented(self):
        """Test if all endpoints are documented"""
        response = self.client.get('/apispec_1.json')
        spec = json.loads(response.data.decode('utf-8'))
        
        # List of required endpoints
        required_endpoints = [
            '/api/v1/documentation/states/[]',
            '/api/v1/documentation/cities',
            '/api/v1/documentation/places',
            '/api/v1/documentation/reviews',
            '/api/v1/documentation/users'
        ]
        
        for endpoint in required_endpoints:
            self.assertIn(endpoint, spec['paths'].keys())

if __name__ == '__main__':
    unittest.main()