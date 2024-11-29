// PLACE DETAILS

// extract the place ID from the query parameters
function getPlaceIdFromURL() {
  const url = new URL(window.location.href);
  console.log(url)
  const placeId = url.searchParams.get('id');
  return placeId;
}

document.addEventListener('DOMContentLoaded', () => {
console.log("ahahah")
fetchPlaceDetails()
});


async function fetchPlaceDetails(token, placeId) {
try {
  const placeId = getPlaceIdFromURL();
  if (placeId == null) {
    return;
  }
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

function displayPlaceDetails(place) {
const detailsContainer = document.getElementById('place-details');
detailsContainer.innerHTML = ''; // vide la liste des anciennes places

// creation des element html pour chaque details

const titleElement = document.createElement('h1');
titleElement.textContent = place.title;

const hostElement = document.createElement('p');
hostElement.textContent = `Host: ${place.owner.first_name} ${place.owner.last_name}`;

const priceElement = document.createElement('p');
priceElement.textContent = `Price per night: $${place.price}`;

const descriptionElement = document.createElement('p');
descriptionElement.textContent = `Description: ${place.description}`;

// list damenities
const amenitiesElement = document.createElement('ul');
place.amenities.forEach(amenity => {
  const li = document.createElement('li');
  li.textContent = amenity.name;
  amenitiesElement.appendChild(li);
});

// reviews
const reviewsElement = document.createElement('div');
place.reviews.forEach(review => {
  const reviewItem = document.createElement('p');
  reviewItem.textContent = `${review.user}: ${review.comment}`;
  reviewsElement.appendChild(reviewItem);
});

 // ajouter les element dans le conteneur
 detailsContainer.appendChild(titleElement);
 detailsContainer.appendChild(hostElement);
 detailsContainer.appendChild(priceElement);
 detailsContainer.appendChild(descriptionElement);
 detailsContainer.appendChild(amenitiesElement);
}