/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/


function checkAuthentication() {
  console.log("xdd")
  const token = getCookie('token');
 return token;
}

window.addEventListener('load', () => {
  console.log("xd")
  const loginLink = document.getElementById('login_button');
  const token = checkAuthentication()
  if (!token) {
    loginLink.style.display = 'block';
} else {
    loginLink.style.display = 'none';
}
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

const logout_button = document.getElementById('logout-btn')
if (logout_button) {
  logout_button.addEventListener('click', logoutUser);
}

function logoutUser() {
  // supprimer le token des cookies
  document.cookie = "token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
  
  // rediriger vers la pagae login
  window.location.href = 'login.html';
}