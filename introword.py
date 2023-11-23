# import streamlit as st 
# import functions 

# st.title('INTROWORDS')
# st.subheader('Share your feelings')

# quotes = functions.read_quotes('quotes.txt')

# # Display quotes as rows
# for idx, quote in enumerate(quotes):
#     st.write(f"feeling {idx+1}: {quote}")

# def add_quote():
#     new_quote = st.session_state.get('new_quote', '').strip()+'\n'
#     if new_quote:
#         quotes.append(new_quote)
#         functions.write_quotes('quotes.txt', quotes)

# # def edit_quote(quote_idx):
# #     edited_quote = st.text_input(label=f"Edit quote {quote_idx + 1}:", value=quotes[quote_idx], key=f'edited_quote_{quote_idx}')
# #     if st.button(label='Update'):
# #         quotes[quote_idx] = edited_quote
# #         functions.write_quotes('quotes.txt', quotes)

# st.text_input(label="", placeholder="Share your feelings...",
#               on_change=add_quote, key='new_quote')
# if st.button(label='Share'):
#     add_quote()  # Adding the quote when the button is clicked




import streamlit as st 
import functions 

st.title('INTROWORDS')
st.subheader('Share your feelings')

quotes = functions.read_quotes('quotes.txt')

for idx, quote in enumerate(quotes):
    st.write(f"Feeling {idx+1}: {quote}")

def add_quote():
    new_quote = st.session_state.get('new_quote', '').strip()+'\n'
    if new_quote:
        quotes.append(new_quote)
        functions.write_quotes('quotes.txt', quotes)

st.text_input(label="", placeholder="Share your feelings...",
              on_change=add_quote, key='new_quote')
if st.button(label='Share'):
    add_quote()

st.markdown(
    """
    <style>
    .social-media {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .social-media a {
        margin: 0 10px;
        text-decoration: none;
        color: #4a4a4a;
    }
    </style>
    """
    , unsafe_allow_html=True)

st.markdown(
    """
    <div class="social-media">
        <a href="https://www.twitter.com/krshxcx">Twitter</a>
        <a href="https://github.com/krshxcx">GITHUB</a>
        <a href="https://www.instagram.com/krshxcx">Instagram</a>
    </div>
    """
    , unsafe_allow_html=True)
