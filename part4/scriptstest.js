document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'https://675c32b6fe09df667f62fe88.mockapi.io/login';
    const API_KEY = 'YOUR_ACTUAL_API_KEY'; // Remplacez par votre vraie clé API

    // Check which page is currently loaded
    const currentPage = document.querySelector('body').className;

    // Places List Page Functionality
    if (document.getElementById('places-list')) {
        setupPlacesFilter();
    }

    // Login Page Functionality
    if (document.getElementById('login-form')) {
        setupLoginForm();
    }

    // Place Details Page Functionality
    if (document.getElementById('place-details')) {
        setupPlaceDetails();
    }

    // Review Form Functionality
    if (document.getElementById('review-form')) {
        setupReviewForm();
    }

    // Function to setup price filtering on places list
    function setupPlacesFilter() {
        const priceFilter = document.getElementById('price-filter');
        const placesCards = document.querySelectorAll('.place-card');

        priceFilter.addEventListener('change', () => {
            const maxPrice = priceFilter.value ? parseInt(priceFilter.value) : Infinity;

            placesCards.forEach(card => {
                const priceText = card.querySelector('.price').textContent;
                const price = parseInt(priceText.replace('$', ''));
                card.style.display = price <= maxPrice ? 'block' : 'none';
            });
        });
    }

    // Simulated login function
    function simulateLogin(email, password) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (email === 'user@example.com' && password === 'password123') {
                    resolve({ access_token: 'fake-jwt-token-' + Date.now() });
                } else {
                    reject(new Error('Invalid email or password'));
                }
            }, 1000);
        });
    }

    // Function to handle login form submission
    function setupLoginForm() {
        const loginForm = document.getElementById('login-form');

        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (!email || !password) {
                alert('Please fill in both email and password');
                return;
            }

            try {
                // Use simulateLogin for testing without a backend
                const data = await simulateLogin(email, password);
                document.cookie = `token=${data.access_token}; path=/; HttpOnly; Secure; SameSite=Strict`;
                window.location.href = 'index.html';
            } catch (error) {
                alert('Login failed: ' + error.message);
            }
        });
    }

    // Function to setup place details page
    function setupPlaceDetails() {
        const amenitiesList = document.querySelector('#place-details ul');
        if (amenitiesList) {
            amenitiesList.querySelectorAll('li').forEach(item => {
                item.classList.add('amenity-item');
            });
        }
    }

    // Function to handle review form submission
    function setupReviewForm() {
        const reviewForm = document.getElementById('review-form');

        reviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const token = getAuthToken();
            if (!token) {
                alert('You must be logged in to submit a review');
                return;
            }

            const reviewText = document.getElementById('review').value;
            const rating = document.getElementById('rating').value;

            if (!reviewText || !rating) {
                alert('Please fill in all required fields');
                return;
            }

            try {
                const response = await fetch(`${API_URL}/reviews`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        text: reviewText,
                        rating: rating
                    })
                });

                if (response.ok) {
                    alert('Review submitted successfully!');
                    reviewForm.reset();
                } else {
                    const errorData = await response.json();
                    alert('Failed to submit review: ' + errorData.message);
                }
            } catch (error) {
                console.error('Review submission error:', error);
                alert('An error occurred while submitting the review.');
            }
        });
    }

    // Helper function to retrieve authentication token
    function getAuthToken() {
        const cookies = document.cookie.split(';');
        const tokenCookie = cookies.find(cookie => cookie.trim().startsWith('token='));
        return tokenCookie ? tokenCookie.split('=')[1] : null;
    }

    // Function to handle logout
    function logout() {
        document.cookie = 'token=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
        window.location.href = 'login.html';
    }
});
