# Book-Data-Scraper
This Python project scrapes book information from [BooksToScrape.com](http://books.toscrape.com/), a website designed for practicing web scraping. It extracts the title, price, star rating, availability, and product URL for each book and saves the data to a CSV file.

## Technologies Used

* **Python 3**
* **Requests:** For fetching the HTML content of web pages.
* **Beautiful Soup 4:** For parsing the HTML content.
* **Pandas:** For data manipulation and saving to CSV.

## Setup

1.  **Clone the repository (if you've uploaded it to GitHub):**
    ```bash
    git clone https://github.com/493g/Book-Data-Scraper
    cd BOOKS_TO_SCRAPE
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    Alternatively, you can install them individually:
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

## How to Run

1.  Navigate to the project directory in your terminal:
    ```bash
    cd BOOKS_TO_SCRAPE
    ```

2.  Execute the main script:
    ```bash
    python main.py
    ```

3.  The script will print the progress of scraping page by page. Once finished, it will:
    * Display the scraped data in the console (as a Pandas DataFrame).
    * Save the data to a CSV file named `books_toscrape_data.csv` in the project directory.

## Output

The scraped data will be stored in a CSV file named `books_toscrape_data.csv`. The file will contain the following columns:

* **Title:** The title of the book.
* **Price (£):** The price of the book in British Pounds.
* **Star Rating:** The star rating of the book (One to Five).
* **Availability:** Whether the book is "In Stock" or "Out of Stock".
* **Product URL:** The URL of the individual book's product page on BooksToScrape.com.

## Ethical Considerations

* This script is designed to scrape a website specifically created for practicing web scraping.
* When scraping other websites, always review their `robots.txt` file and terms of service to understand their policies on automated access.
* Be respectful of website resources by including delays between requests (`time.sleep()`) to avoid overloading their servers.
* Use web scraping responsibly and ethically.

## Further Enhancements (Optional)

* **Error Handling:** Implement more robust error handling for network issues and changes in website structure.
* **More Data:** Extract additional information from the book pages (e.g., product description, category, number of reviews).
* **User Configuration:** Allow users to specify the number of pages to scrape or filter by rating.
* **Data Storage:** Store the data in a database instead of a CSV file.


