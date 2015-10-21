import urllib, json

file_movie_quotes = "movie_quotes.txt"
url_wdyl_profanity = "http://www.wdyl.com/profanity?q="

def read_text():
    quotes = open(file_movie_quotes)
    # If we want to strip new lines, we can go line-by-line via for loop.
    #all_text = ""
    #for line in quotes:
    #    all_text = all_text + line.strip() + " "
    #print all_text
    file_contents = quotes.read()
    quotes.close()
    check_profanity(file_contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen(url_wdyl_profanity + text_to_check)
    data = json.load(connection)
    connection.close()
    if data.get("response") == "false":
        print "No profanity here!"
    elif data.get("response") == "true":
        print "Hey, watch your mouth!"
    else:
        print "Could not scan the document properly."

read_text()
