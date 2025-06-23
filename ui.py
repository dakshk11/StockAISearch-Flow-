import streamlit as st
from backend import search_stocks, get_posts, create_post

# Streamlit app configuration
st.set_page_config(page_title="Stocker", page_icon="📈")
st.title("Stocker: Stock Price, News, and API Interface")

# Initialize session state for API key
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# API key input
api_key = st.text_input("Enter your Firecrawl API Key:", type="password", value=st.session_state.api_key)
st.session_state.api_key = api_key

# Sidebar for navigation
st.sidebar.header("Navigation")
option = st.sidebar.selectbox("Choose Action", ["Search Stocks", "Fetch Posts (GET)", "Create Post (POST)"])

# Main app logic
if api_key:
    try:
        if option == "Search Stocks":
            st.header("Search Stock Price and News")
            company_name = st.text_input("Enter company name (e.g., Apple):")
            token = st.text_input("Enter company token (e.g., AAPL):")

            if st.button("Search") and company_name and token:
                with st.spinner("Searching for stock price and news..."):
                    crawl_result = search_stocks(api_key, company_name, token)
                    if crawl_result and isinstance(crawl_result, list):
                        st.subheader("Search Results")
                        for idx, result in enumerate(crawl_result, 1):
                            with st.expander(f"Result {idx}: {result.get('title', 'No Title')}", expanded=True):
                                st.markdown(result.get("markdown", "No markdown content available"))
                                st.write(f"**Source URL:** {result.get('url', 'No URL')}")
                    else:
                        st.warning("No results found or unexpected response format.")

            elif company_name or token:
                st.warning("Please provide both company name and token.")

        elif option == "Fetch Posts (GET)":
            st.header("Fetch Sample Posts (GET Request)")
            post_id = st.text_input("Enter Post ID (leave blank for all posts):")

            if st.button("Fetch Posts"):
                with st.spinner("Fetching posts..."):
                    result = get_posts(post_id if post_id else None)
                    if "error" in result:
                        st.error(f"Error: {result['error']}")
                    else:
                        st.subheader("Posts")
                        st.json(result)

        elif option == "Create Post (POST)":
            st.header("Create a New Post (POST Request)")
            with st.form(key="create_post_form"):
                title = st.text_input("Post Title")
                body = st.text_area("Post Body")
                user_id = st.number_input("User ID", min_value=1, value=1)
                submit_button = st.form_submit_button("Create Post")

                if submit_button:
                    if not title or not body:
                        st.warning("Please fill in all fields.")
                    else:
                        with st.spinner("Creating post..."):
                            result = create_post(title, body, user_id)
                            if "error" in result:
                                st.error(f"Error: {result['error']}")
                            else:
                                st.success("Post created successfully!")
                                st.json(result)

    except Exception as e:
        st.error(f"Error: {str(e)}. Please check your API key or try again.")

else:
    st.info("Please enter a valid Firecrawl API key to proceed.")

# Footer
st.markdown("---")
st.markdown("Powered by Firecrawl, JSONPlaceholder, and Streamlit")