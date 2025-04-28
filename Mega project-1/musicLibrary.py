# # music = {
# #     "kalank" : "https://youtu.be/Grr0FlC8SQA?si=dqWSK4Fsi5cqzL7h",
# #     "kakan" : "https://youtu.be/7oNdJ_SmD8o?si=N0y-0ar6MNGd-j9v"
# # }

# import requests
# news_api_key = "671d6e09436d4b2782e11d42a34734ec"

# import requests
# news_api_key = "671d6e09436d4b2782e11d42a34734ec"

# def news():
#     url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=671d6e09436d4b2782e11d42a34734ec"
#     r = requests.get(url)
    
#     if r.status_code == 200:
#         data = r.json()
#         articles = data.get('articles', [])

#         if articles:
#             for i, article in enumerate(articles, start=1):
#                 title = article.get('title', 'No title available')
#                 print(f"{i}. {title}")
#         else:
#             print("No articles found.")
#     else:
#         print("Failed to fetch news.")

# # Call function
# news()

