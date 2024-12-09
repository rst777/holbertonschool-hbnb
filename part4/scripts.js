document.addEventListener('DOMContentLoaded', () => {
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

  // Price Filter for Places List
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

  // Login Form Validation
  function setupLoginForm() {
      const loginForm = document.getElementById('login-form');

      loginForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const email = document.getElementById('email').value;
          const password = document.getElementById('password').value;

          // Basic validation
          if (!email || !password) {
              alert('Please fill in both email and password');
              return;
          }

          // Simulated login (replace with actual authentication logic)
          if (isValidLogin(email, password)) {
              alert('Login Successful!');
              // Redirect to index page or dashboard
              window.location.href = 'index.html';
          } else {
              alert('Invalid email or password');
          }
      });
  }

  // Simulated Login Validation
  function isValidLogin(email, password) {
      // This is a dummy validation - replace with real authentication
      return email === 'user@example.com' && password === 'password123';
  }

  // Place Details Page Setup
  function setupPlaceDetails() {
      // Example: Highlight amenities
      const amenitiesList = document.querySelector('#place-details ul');
      if (amenitiesList) {
          amenitiesList.querySelectorAll('li').forEach(item => {
              item.classList.add('amenity-item');
          });
      }
  }

  // Review Form Handling
  function setupReviewForm() {
      const reviewForm = document.getElementById('review-form');

      reviewForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const reviewText = document.getElementById('review-text').value;
          const rating = document.getElementById('rating') ?
                         document.getElementById('rating').value : null;

          // Basic validation
          if (!reviewText || (rating && rating === '')) {
              alert('Please fill in all required fields');
              return;
          }

          // Simulated review submission
          submitReview(reviewText, rating);
      });
  }

  // Simulated Review Submission
  function submitReview(text, rating) {
      // In a real app, this would send data to a server
      const newReview = {
          text: text,
          rating: rating,
          date: new Date().toLocaleDateString(),
          author: 'Current User' // Would be dynamically set in a real app
      };

      // For demonstration: log review and show success message
      console.log('Review Submitted:', newReview);
      alert('Thank you for your review!');

      // Reset form
      document.getElementById('review-form').reset();
  }
});
