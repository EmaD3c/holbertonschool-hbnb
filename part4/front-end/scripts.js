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

  console.log(response)
  // si la reponse a la requete est positive
  if (response.ok) {
    const data = await response.json();
    const token = data.access_token;
    // Le token JWT est stocke dans un cookie
    document.cookie = `token=${token}; path=/`;
    console.log({token})
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
  console.log("xdd")
  const token = getCookie('token');
  const loginLink = document.getElementById('login_button');

  if (!token) {
      loginLink.style.display = 'block';
  } else {
      loginLink.style.display = 'none';
      // si l'user est identifier fetch la place
      fetchPlaces(token);
  }
}

window.addEventListener('load', () => {
  console.log("xd")
  checkAuthentication()
});

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
  fetch("http://127.0.0.1:5000/api/v1/places/")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Data recovery error");
      }
      return response.json();
    })
    .then((data) => {
      displayPlaces(data);
    })
    .catch((error) => {
      console.error("Erreur :", error);
    });
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
      <p>${place.title}</p>
      <p>Price per night: $${place.price}</p>
      <a href="place.html?id=${place.id}" class="button login_button">View Details</a>
    `;
    
    placeCard.innerHTML = placeInfo;

    // ajoute la carte au conteneur de la liste
    placesList.appendChild(placeCard);
  });
}


// PLACE DETAILS

function getPlaceIdFromURL() {
  const mySearchParams = new URLSearchParams(window.location.search);
  return mySearchParams.get('id'); // recuperer la valeur de "id"
}


async function fetchPlaceDetails(token, placeId) {
  try {
    const placeId = getPlaceIdFromURL();
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    if (response.ok) {
      const place = await response.json();
      displayPlaceDetails(place);
    } else {
      console.error('Error when retrieving place details');
    }
  } catch (error) {
    console.error('Error :', error);
  }
}
