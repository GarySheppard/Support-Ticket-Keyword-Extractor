#Necessary installations
'''
pip install rake-nltk
pip install openpyxl
pip install pandas
'''

import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake

# Initialize the Rake object
r = Rake(
    min_length = 1,
    max_length = 8
)

# Convert the support ticket data to a Pandas DataFrame, filtering out feature requests
df = pd.read_excel('Support Ticket Dataset.xlsx')
df = df[df['Category'] != 'Feature Request']

# Extract only the support ticket descriptions from the DataFrame
desc_series = df['Description']
descs = df['Description'].values.tolist()

# Extract keywords from the descriptions, ranking them by relevance
r.extract_keywords_from_sentences(descs)
keywords = r.get_ranked_phrases_with_scores()

# Write extracted keywords and their scores to an Excel file
keyword_data = {
    'Support Ticket Excerpt': [],
    'Relevance Score': []
}
for score, keyword in keywords:
    keyword_data['Support Ticket Excerpt'].append(keyword)
    keyword_data['Relevance Score'].append(score)
keyword_df = pd.DataFrame(keyword_data)
keyword_df = keyword_df.drop_duplicates(subset = ['Support Ticket Excerpt'])
keyword_df.to_excel('Support Ticket Keywords.xlsx', index = False)