# Import Dependencies
import pandas as pd


# Make a reference to the books.csv file path
filepath = os.path.join("D:\Github\Web_Design_Challenge\Resources\cities.csv")

# Import the books.csv file as a DataFrame
df = pd.read_csv(filepath, encoding="utf-8")

#df.reset_index(inplace=True, drop=True)
df.head()

#create html tbale
html_table = df.to_html()


#write html table to text
text_file = open("datan.html", "w")
text_file.write(html_table)
text_file.close()
