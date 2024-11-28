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
  // supprimer le token des cookies
  document.cookie = "token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
  
  // rediriger vers la pagae login
  window.location.href = 'login.html';
}


// INDEX

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
      loginLink.style.display = 'block';
  } else {
      loginLink.style.display = 'none';
      // su l'user est identifier fetch la place
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

async function fetchPlaces(token) {
  try {
      // requete
      const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
          method: 'GET',
          headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
          }
      });

      if (!response.ok) {
          throw new Error('Erreur lors de la récupération des données');
      }

      // Conversion de la réponse en JSON
      const places = await response.json();
      // afficher les lieux
      displayPlaces(places);
  } catch (error) {
      console.error('Erreur Fetch:', error.message);
  }
}

function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  placesList.innerHTML = ''; // vide la liste des anciennes places

  // pour chaque place ca cree element HTML
  places.forEach(place => {
    // carte pour chaque place
    const placeCard = document.createElement('div');
    placeCard.classList.add('cards', 'place-card');

    // contenu HTML a inserer dans la carte
    const placeInfo = `
      <p>${place.name}</p>
      <p>Price per night: $${place.price}</p>
      <a href="place.html?id=${place.id}" class="button login-button">View Details</a>
    `;
    
    placeCard.innerHTML = placeInfo;

    // ajoute la carte au conteneur de la liste
    placesList.appendChild(placeCard);
  });
}
