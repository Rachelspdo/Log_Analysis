import psycopg2

DBNAME = "news"

# Most Three Popular Articles

query_1 ="SELECT * FROM Summary LIMIT 3;"

# Find the most popular article authors

query_2 ="SELECT Popular_author.author, authors.name, Popular_author.Total_Views FROM authors, Popular_author WHERE authors.id = Popular_author.author;"

# Find the day which has more than 1% or 0.01 of requests lead to errors

query_3="SELECT DATE_REQUEST, (1.00 * TOTAL_ERRORS / TOTAL_REQUESTS) as PECG FROM Access_Summary_By_Date WHERE (1.00 * TOTAL_ERRORS / TOTAL_REQUESTS) > 0.01;"


def get_query_result(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_1)
    results = c.fetchall()
    db.close()
    print ("Popular Articles:")
    for row in rows:
        print ("", row[0])
    return results




















