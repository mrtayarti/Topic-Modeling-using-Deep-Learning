import pandas as pd
from lda2vec.nlppipe import Preprocessor

# Data directory
data_dir ="data"
# Where to save preprocessed data
clean_data_dir = "data/clean_data"
# Name of input file. Should be inside of data_dir
input_file = "news.csv"
# Should we load pretrained embeddings from file
load_embeds = True

# Read in data file
df = pd.read_csv(data_dir+"/"+input_file, sep=",")

print(df)
# Initialize a preprocessor
P = Preprocessor(df, "headline_text", token_type="lower", max_features=10000,
                 maxlen=10000, min_count=30, nlp="en_core_web_lg")

# Run the preprocessing on your dataframe
P.preprocess()

# Load embeddings from file if we choose to do so
if load_embeds:
    # Load embedding matrix from file path - change path to where you saved them
    embedding_matrix = P.load_glove("glove.6B.300d.txt")
else:
    embedding_matrix = None

# Save data to data_dir
P.save_data(clean_data_dir, embedding_matrix=embedding_matrix)
