document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const signupForm = document.getElementById('signup-form');

  // Gestion de la soumission du formulaire de connexion
  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault(); // Empêche le comportement par défaut

          const email = loginForm.querySelector('input[name="email"]').value;
          const password = loginForm.querySelector('input[name="password"]').value;

          await loginUser(email, password);
      });
  }

  // Gestion de la soumission du formulaire d'inscription
  if (signupForm) {
      signupForm.addEventListener('submit', async (event) => {
          event.preventDefault(); // Empêche le comportement par défaut

          const email = signupForm.querySelector('input[name="email"]').value;
          const password = signupForm.querySelector('input[name="password"]').value;

          await registerUser(email, password);
      });
  }
});

// Fonction pour se connecter
async function loginUser(email, password) {
  try {
      const response = await fetch('https://your-api-url/login', { // Remplacez par l'URL de votre API
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
          throw new Error('Erreur de connexion');
      }

      const data = await response.json();
      console.log('Connexion réussie:', data);
  } catch (error) {
      console.error('Erreur:', error);
  }
}

// Fonction pour s'inscrire
async function registerUser(email, password) {
  try {
      const response = await fetch('https://your-api-url/register', { // Remplacez par l'URL de votre API
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
          throw new Error('Erreur d\'inscription');
      }

      const data = await response.json();
      console.log('Inscription réussie:', data);
  } catch (error) {
      console.error('Erreur:', error);
  }
}
