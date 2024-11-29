// INDEX

let places = []

const token = checkAuthentication()
if (token){
  fetchPlaces(token)
  .then((data) => {
    console.log(data)
    places = data;
    displayPlaces(places);
  })
  .catch((error) => {
    console.error("Erreur :", error);
  });
}

async function fetchPlaces(token) {
  return fetch("http://127.0.0.1:5000/api/v1/places/")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Data recovery error");
      }
      return response.json();
    })
  }

function displayPlaces(places, max_price) {
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

const price_filter = document.getElementById('price-filter')
if (price_filter) {
  price_filter.addEventListener('change', filterplaces);
}

function filterplaces(event) {
  // deux argument different 
  const value = event.target.value;
  console.log(value)
  const filtered_places = places.filter(place => place.price <= value || value == 0)
  displayPlaces(filtered_places);
}