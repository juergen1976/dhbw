document.getElementById('search-button').addEventListener('click', function() {
    let query = document.getElementById('search-input').value;
    searchSongs(query);
});

function searchSongs(query) {
    const corsProxy = 'https://cors-anywhere.herokuapp.com/';
    const apiUrl = `https://api.deezer.com/search?q=${query}&limit=5`;

    fetch(corsProxy + apiUrl)
        .then(response => response.json())
        .then(data => displayResults(data))
        .catch(error => console.error('Error:', error));
}

function displayResults(data) {
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    data.data.forEach(song => {
        let songDiv = document.createElement('div');
        songDiv.classList.add('song');

        let img = document.createElement('img');
        img.src = song.album.cover_small;
        songDiv.appendChild(img);

        let infoDiv = document.createElement('div');
        infoDiv.classList.add('song-info');

        let title = document.createElement('h4');
        title.textContent = song.title;
        infoDiv.appendChild(title);

        let artist = document.createElement('p');
        artist.textContent = song.artist.name;
        infoDiv.appendChild(artist);

        songDiv.appendChild(infoDiv);

        let audio = document.createElement('audio');
        audio.controls = true;
        audio.src = song.preview;
        songDiv.appendChild(audio);

        resultsDiv.appendChild(songDiv);
    });
}
