import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
BASE_URL = "http://books.toscrape.com/"

# Function to extract book data from a book container
def extract_book_data(book_container):
    title_element = book_container.h3.a
    title = title_element['title'].strip() if title_element and 'title' in title_element.attrs else "N/A"

    price_element = book_container.find('p', class_='price_color')
    price = price_element.text.strip() if price_element else "N/A"

    rating_classes = book_container.find('p', class_='star-rating')
    rating = "N/A"
    if rating_classes and 'star-rating' in rating_classes['class']:
        if 'One' in rating_classes['class']:
            rating = 'One'
        elif 'Two' in rating_classes['class']:
            rating = 'Two'
        elif 'Three' in rating_classes['class']:
            rating = 'Three'
        elif 'Four' in rating_classes['class']:
            rating = 'Four'
        elif 'Five' in rating_classes['class']:
            rating = 'Five'

    availability_element = book_container.find('p', class_='instock availability')
    availability_text = availability_element.text.strip() if availability_element else "N/A"
    availability = "In Stock" if "In stock" in availability_text else "Out of Stock"

    relative_url = title_element['href'] if title_element and 'href' in title_element.attrs else None
    product_url = f"{BASE_URL}catalogue/{relative_url.replace('../', '')}" if relative_url else "N/A"

    return {
        'Title': title,
        'Price (£)': price,
        'Star Rating': rating,
        'Availability': availability,
        'Product URL': product_url
    }

# Main function to scrape book listings from all pages
def scrape_all_books():
    all_books_data = []
    page_num = 1
    while True:
        url = f"{BASE_URL}catalogue/page-{page_num}.html"
        print(f"Scraping page: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            book_containers = soup.find_all('article', class_='product_pod')

            if not book_containers:
                print("No more book listings found.")
                break

            for container in book_containers:
                book_data = extract_book_data(container)
                all_books_data.append(book_data)

            page_num += 1
            time.sleep(1)  # Be respectful
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            break
        except Exception as e:
            print(f"An error occurred while parsing page {page_num}: {e}")
            break
    return all_books_data

if __name__ == "__main__":
    import time

    print("Starting to scrape book information from BooksToScrape.com...")
    start_time = time.time()
    all_books = scrape_all_books()
    end_time = time.time()
    print(f"Scraping completed in {end_time - start_time:.2f} seconds.")

    if all_books:
        df = pd.DataFrame(all_books)
        print("\nScraped Book Data:")
        print(df)

        # Save to CSV
        csv_filename = "books_toscrape_data.csv"
        df.to_csv(csv_filename, index=False, encoding='utf-8')
        print(f"\nData saved to {csv_filename}")
    else:
        print("No book data scraped.")