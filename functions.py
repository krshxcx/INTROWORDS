Filepath = 'quotes.txt'

def read_quotes(Filepath):
    with open(Filepath,'r') as file:
        quotes = file.readlines()
        return quotes

def write_quotes(Filepath,quotes):
      with open(Filepath,'w') as file:
          file.writelines(quotes)
          