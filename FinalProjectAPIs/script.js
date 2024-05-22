
async function searchBooks() {
    const searchInput = document.getElementById('searchInput').value;
    const apiUrl = `https://www.googleapis.com/books/v1/volumes?q=${searchInput}`;

    try {
        const response = await axios.get(apiUrl);
        displayBooks(response.data.items);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

async function fetchBookDetails(bookId) {
    const apiUrl = `https://www.googleapis.com/books/v1/volumes/${bookId}`;

    try {
        const response = await axios.get(apiUrl);
        displayBooks(bookId, response.data.volumeInfo);
    } catch (error) {
        console.error('Error fetching book details:', error);
    }
}

async function displayBooks(books) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    books.forEach(book => {
        const bookInfo = book.volumeInfo;
        const bookDiv = document.createElement('div');
        bookDiv.classList.add('book');

        const image = bookInfo.imageLinks ? `<img src="${bookInfo.imageLinks.thumbnail}" alt="Book Cover">` : '';
        const title = bookInfo.title ? `<h2>${bookInfo.title}</h2>` : '';
        const authors = bookInfo.authors ? `<p>Author(s): ${bookInfo.authors.join(', ')}</p>` : '';

        const summary = bookInfo.description ? `<p class="summary">${bookInfo.description}</p>` : '';
        const genre = bookInfo.categories ? `<p>Genre(s): ${bookInfo.categories.join(', ')}</p>` : '';

        const showMoreButton = `<button class="show-more" onclick="toggleSummary(this)">View More</button>`;

        bookDiv.innerHTML = `${image} ${title} ${authors} ${showMoreButton} ${summary} ${genre}`;
        resultsDiv.appendChild(bookDiv);
    });
}

function toggleSummary(button) {
    const summary = button.parentNode.querySelector('.summary');
    summary.style.display = summary.style.display === 'none' ? 'block' : 'none';
}
