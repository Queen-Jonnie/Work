# First, i imported the libraries i'll be making use of.
import requests
import bs4
import sys
import time


# The get_valid_page() function below helps me get the correct page number for the webpage I am trying to access


def get_valid_page(n):
    pages = 2
    if n == 0 or n > pages:
        print("Sorry, this web page only have 2 pages. You can only check books on page 1 and 2")
        sys.exit()


page = 1
get_valid_page(page)

# Here i am announcing the URL that holds the data I am trying to access, and fetching the data.
url = f"https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg={page}"


print("Fetching data from webpage\n")
time.sleep(2)

# I have now wrapped the entire program in a try and exception to help me catch any errors in running the program


try:

    """
    I am headers because some servers only allow specific user-agent strings.
    The server might specifically block requests, or they might utilize a whitelist, or some other reason.
    Passing header into the .get() will help solve this problem.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 '
                      'Safari/537.36',
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }

    response = requests.get(url, headers=headers, params={"wait": 2})

    soup = bs4.BeautifulSoup(response.text, 'lxml')

# Below i created a Book component where all books information can be found.
# I then used .select() method in beautiful soup to select the HTML tag and class

    book_item = soup.select(".zg-item-immersion")


#  I made an empty list to add all the popular books we have selected from the webpage using BeautifulSoup
    most_rated_books = []
#  I then created a loop through my book component where i basically stated that if the book is a 5 star rated,
#  then get the book.
    for book in book_item:
        if "a-star-5" in str(book):
            for book_names in book.select(".p13n-sc-truncate"):
                most_rated_books.append(book_names.getText().strip())


#  Next, I created an empty list to hold the prices of the popular books.
    most_rated_books_prices = []
    for book in book_item:
        if "a-star-5" in str(book):
            for prices in book.find(name="span", class_="p13n-sc-price"):
                most_rated_books_prices.append(float(prices.replace("$", "")))


# Below, i created an empty list to hold the sorted prices we get and a loop through the initial prices list to get
# the top 10 from lowest to highest. I also set my max_range to 10; to get the top ten.
    top_ten_prices = []
    for price in most_rated_books_prices:
        top_ten_prices.append(price)
    max_range = 10
    top_ten_prices.sort()
    top_ten_prices = top_ten_prices[-max_range:]


# I have now acquired the prices of the ten most expensive books but i need to get the names of those books so i made
# an empty list to hold the values.
    ten_most_expensive = []

# I am doing this "unsorted_prices" below so i can compare it with the ten_most_expensive returns and make a
# dictionary that holds books and their prices, after which i'll create a loop through the book component.

    unsorted_prices = []
    for book in book_item:
        if "a-star-5" in str(book):
            for val in top_ten_prices:
                if f"${val}" in str(book):
                    ten_most_expensive.append((book.find(name="div", class_="p13n-sc-truncate").text.strip()))
                    for prices in book.find(name="span", class_="p13n-sc-price"):
                        unsorted_prices.append(prices)

# Iam using a dictionary comprehension syntax to save the names of the most expensive books and their fees in a "final_
# result" variable. The final_result variable returns our top 10 most costly popular books with the most reviews as a
# list. Which i can mow print out.

    final_result = [{ten_most_expensive[i]: unsorted_prices[i] for i in range(len(ten_most_expensive))}]

    print(final_result)

except requests.exceptions.RequestException as e:
    print("Something went wrong. Please check the your internet connection or URL\n", e)
