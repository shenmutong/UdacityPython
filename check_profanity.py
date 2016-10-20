def read_text():
      quotes = open(r"E:\CurrentWork\PythonPlayground\checkprofanityFile\movie_quotes.txt")
      contents_of_file = quotes.read()
      print (contents_of_file)
      quotes.close()

read_text()