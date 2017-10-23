import psycopg2

DBNAME = "news"



# get_query_result function is used to execute a SQL query

def get_query_result(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query_1)
        results = c.fetchall()
        db.close()
        return results

# Get the top three articles by views

def top_three_popular_articles():
    query_1 ="SELECT * FROM Summary LIMIT 3;"
    popular_articles= get_query_result(query_1)
    print('Question 1: Most popular three articles of all times:")
    for i in popular_articles:
          print('"' + i[0] + '"' + ' -- ' + str(i[1]) + 'views')
          print(' ')

print(' ')

# Get total of all articles views by each author
          
def most_popular_article_authors():
    query_2 ="""SELECT Popular_author.author, authors.name, Popular_author.Total_Views
    FROM authors, Popular_author
    WHERE authors.id = Popular_author.author;"""
    popular_author= get_query_result(query_2)
    print('Question 2: The most popular article authors of all time:')
    for i in popular_author:
          print('"' + i[0] + '"' + ' -- ' + str(i[1]) + 'views')
          print(' ')
          
print(' ')

# The day has more than 1% requests lead to error

def day_with_perg_error():
    query_3="""SELECT DATE_REQUEST, (1.00 * TOTAL_ERRORS / TOTAL_REQUESTS) as PECG
    FROM Access_Summary_By_Date
    WHERE (1.00 * TOTAL_ERRORS / TOTAL_REQUESTS) > 0.01;"""
    error_day = get_query_result(query_3)
    print('Question 3: The day has more than 1% requests lead to error:')
    for i in error_day:
          print(i[0] + " -- " + i[1] + '%' + ' error')

          



















