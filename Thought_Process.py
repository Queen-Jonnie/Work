# When I first reviewed the question, I felt like I could quickly just get the prices of the books on both pages and
# sort them from the highest to the least expensive price and get my top ten books from there, so I started by using
# urllib library, but that didn't work out with the URL provided so I moved on to bs4 a request libraries bs4 because it
# allowed me to get the text from a website to my IDE in a readable format and request because it helps the IDE connect
# to the URL in which we would need data from before the bs4 library can take information from there. This commenced for
# a while and went great until I reread the question and realized I had misunderstood it.

# I realized that arranging the book prices for the two pages from highest to lowest didn't necessarily mean that those
# books were among the most popular books or the books with many reviews. I also found that all the books were ranked by
# popularity, and if that was the case, the second page didn't have any relevance to the question. So, I changed my
# focus to only the price of the books on the first page. However, just doing that wasn't enough as it didn't satisfy
# the "many reviews'' requirement, so I decided to get the list of the books reviews first then sort it out from the one
# with the most reviews to the least, after which I can now sort out the prices to find out the top 10 most expensive
# books. So I did just that, but in sorting the reviews,  I got stuck because the commas in the numbers were giving me
# issues, and I couldn't progress to the next phase. After struggling with it for a while, I decided to start afresh and
# include some new libraries to the ones I was using, so I also imported sys and time libraries.

# Sys library provides various functions and variables that a programmer can use to manipulate different parts of the
# Python runtime environment and time library. It offers many ways of representing time in code, such as objects,
# numbers, and strings. It also includes functionality other than representing time, like waiting during code execution
# and measuring the efficiency of your code. I first created a get_valid_page() function to help get the correct page
# number for the webpage I was trying to access. Then I announced the URL we are trying to access to get data, after
# which I fetched the data from the webpage. I also wrapped the entire program in a try and exception block; this helped
# me catch any errors in running my program.

# Moreover, I put headers because some servers only allow specific user-agent strings, so I passed the header into
# the .get() to solve this problem. I then used the request.get() to get the web page URL I wanted to focus on.
# In addition, I made a book component where a user can find all books' information. From then on, I created lists and
# for loops for the most rated books, the most rated books prices, a loop through the initial prices list, a loop though
# the book component get the ten most expensive books, and a dictionary comprehension syntax to save the names of
# books and their fees in a final_result variable. The final_result variable returns our top 10 most costly popular
# books with the most reviews as a list. Then I printed it, and it worked out beautifully.
