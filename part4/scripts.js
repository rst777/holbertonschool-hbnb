document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'https://675d438bfe09df667f65cc4a.mockapi.io/login'; 
    // Configuration de l'écouteur d'événements pour le formulaire de connexion
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault(); // Empêche le comportement par défaut du formulaire

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Validation basique des entrées
            if (!email || !password) {
                alert('Veuillez remplir les champs email et mot de passe');
                return;
            }

            try {
                // Faire une requête AJAX vers l'API
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email, password }) // Utiliser les valeurs saisies par l'utilisateur
                });

                // Gérer la réponse de l'API
                if (response.ok) {
                    const data = await response.json();
                    // Stocker le jeton JWT dans un cookie
                    document.cookie = `token=${data.access_token}; path=/; Secure; SameSite=Strict`;
                    // Rediriger vers la page principale
                    window.location.href = 'index.html';
                } else {
                    const errorData = await response.json();
                    alert('Échec de la connexion : ' + errorData.message);
                }
            } catch (error) {
                console.error('Erreur lors de la connexion :', error);
                alert('Une erreur est survenue lors de la connexion. Veuillez réessayer.');
            }
        });
    }
});
