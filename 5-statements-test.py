# Statement Assessment Test

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'

st = 'Print only the words that start with s in this sentence'
for words in st.split():
    if words[0] == 's':
        print(words)

