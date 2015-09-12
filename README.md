# Summarizer
A summarization algorithm written in python. Takes in a json object containing the data and summarization parameters and returns a summary and the key terms. This is the code I wrote for this algorithm on aglorithmia: https://algorithmia.com/algorithms/kasandell/Summarizer.
This algorithm is the summarization algorithm from my app: https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=962626932 translated into python.

Summarizer is an algorithm that takes in data and json format and returns a summary and key terms from the text. The json object the algorithm takes needs 4 fields:

text: a string containing the text you want summarized

summaryLength: a floating point number, less than or equal to one, which represents a percentage of the text length you want the summary to be

keyTermsWanted: a boolean, with true meaning you want the key terms from the algorithm, and false meaning you don't

numKeyTerms: an integer, representing the number of key terms you want from the text.



The output returns a json object with 1 or two fields, depending on if you want the key terms. The object contains:

summary: a list, containing the strings that make up the summary. The sentences are ranked in order of importance; the first sentence is the most important. This is guaranteed to be part of the returned object.

keyTerms: a list, containing the number of key terms requested, if they are requested. The key terms are ranked in order of importance; the first term is the most important. This is only part of the returned json object if 'keyTermsWanted' is true in the input json object.



Below is an easy to use json object that you only need to paste the variables into to use.

"{\"text\": \"TEXT\", \"summaryLength\": floatingPointPercentage, \"keyTermsWanted\": boolean, \"numKeyTerms\": numberOfKeyTermsWanted}"
