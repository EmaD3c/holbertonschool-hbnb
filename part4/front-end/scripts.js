/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

// LOGIN

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      // recupere les donneee de l'user 
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      await loginUser(email, password);
    });
  }
});

// requete post a l'api avec les doneee de conexion (email, password)
async function loginUser(email, password) {
  const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // transforme un onjet js en chaine json
    body: JSON.stringify({ email, password }),
  });

  // si la reponse a la requete est positive
  if (response.ok) {
    const data = await response.json();
    const token = data.token;
    // Le token JWT est stocke dans un cookie
    document.cookie = `token=${token}; path=/`;
    // Et l'utilisateur revient à la page d'accueil
    window.location.href = 'index.html';
  } else {
    alert('Login failed');
  }
}

document.getElementById('logout-btn').addEventListener('click', logoutUser);

function logoutUser() {
  // Supprimer le token des cookies
  document.cookie = "token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
  
  // Rediriger vers la page de connexion ou une autre page
  window.location.href = 'login.html'; // ou 'index.html'
}


// INDEX

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
      loginLink.style.display = 'block';
  } else {
      loginLink.style.display = 'none';
      // Fetch places data if the user is authenticated
      fetchPlaces(token);
  }
}
function getCookie(name) {
  // .split(';') divise la chaine en un tableau de cookie individuel
  const cookies = document.cookie.split(';');
  for (const cookie of cookies) {
    // .trim() enleve les espaces inutiles autour du cookie
      const [key, value] = cookie.trim().split('=');
      if (key === name) return value;
  }
  return null;
}

