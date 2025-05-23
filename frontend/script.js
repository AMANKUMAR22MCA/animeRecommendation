const baseUrl = 'http://127.0.0.1:8001';
const token = localStorage.getItem('access_token');

document.getElementById('logoutBtn').onclick = () => {
  localStorage.clear();
  window.location.href = 'login.html';
};

function savePreferences() {
  const checkboxes = document.querySelectorAll('input[type=checkbox]:checked');
  const genres = Array.from(checkboxes).map(cb => cb.value);

  fetch(`${baseUrl}/user/preferences/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ favorite_genres: genres })
  }).then(res => res.json()).then(data => {
    alert('Preferences saved!');
    getRecommendations();
  });
}

function searchAnime() {
  const query = document.getElementById('searchInput').value;

  fetch(`${baseUrl}/anime/search/?q=${encodeURIComponent(query)}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  }).then(res => res.json()).then(data => {
    const media = data.data?.Page?.media || [];
    const container = document.getElementById('searchResults');
    container.innerHTML = '';
    media.forEach(anime => {
      container.innerHTML += renderAnimeCard(anime);
    });
  });
}



function getRecommendations() {
  const container = document.getElementById('recommendationList');
  container.innerHTML = '<p>Loading recommendations...</p>';

  fetch(`${baseUrl}/anime/recommendations/`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
    .then(res => res.json())
    .then(data => {
      console.log("Recommendation API response:", data);
      const media = data.recommendations || [];
      container.innerHTML = ''; // clear loading text

      if (media.length === 0) {
        container.innerHTML = '<p>No recommendations yet. Set your preferences above!</p>';
        return;
      }

      media.forEach(anime => {
        container.innerHTML += renderAnimeCard(anime);
      });
    })
    .catch(err => {
      console.error("Error fetching recommendations:", err);
      container.innerHTML = '<p>Error loading recommendations. Please try login again....</p>';
    });
}



function renderAnimeCard(anime) {
  const title = anime.title?.english || anime.title?.romaji || "No title";
  return `
    <div class="anime-card">
      <h4>${title}</h4>
      <p>${anime.genres.join(', ')}</p>
      <p><strong>Popularity:</strong> ${anime.popularity}</p>
    </div>
  `;
}
// Load recommendations on page load
getRecommendations();
