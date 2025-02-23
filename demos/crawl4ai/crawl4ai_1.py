import asyncio
from crawl4ai import AsyncWebCrawler  # Utilise AsyncWebCrawler de crawl4ai
from pydantic import BaseModel
from typing import List
import markdownify
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

# Définition de la classe Pydantic pour structurer un blog post
class BlogPost(BaseModel):
    title: str       # Titre en Markdown
    content: str     # Contenu en Markdown
    link: str        # URL de l'article

class linkItem (BaseModel):
    link: str

async def fetch_blog_posts(base_url: str) -> list[BlogPost]:
    posts = []
    # Utilisation d'AsyncWebCrawler dans un contexte asynchrone
    async with AsyncWebCrawler(start_url=base_url) as crawler:
        # Récupération de la page d'index et extraction du contenu HTML
        index_result = await crawler.arun(base_url)
        data = index_result.links  # On récupère les liens des blog posts
        hrefs = []
        print (data)
        print(isinstance(data, dict))
        data_internal = data.get("internal")
        print(isinstance(data_internal,List))
        Internal_list = data_internal
        print(Internal_list)
        print(len(Internal_list))
        print(Internal_list[0].get("href"))
        for i in range(len(Internal_list)):
            if "blog/" in Internal_list[i].get("href") :
                print(Internal_list[i].get("href"))
    
                


        # # soup = BeautifulSoup(index_html, 'html.parser')
        
        # # Extraction des liens des articles de blog (à adapter selon la structure du site)
        # blog_links = []
        # for a in soup.find_all('a', href=True):
        #     href = a['href']
        #     if '/blog/' in href:
        #         absolute_url = urljoin(base_url, href)
        #         blog_links.append(absolute_url)
        # blog_links = list(set(blog_links))  # Éliminer les doublons
        
        # for link in blog_links:
        #     try:
        #         # Récupération de la page de l'article et extraction du HTML
        #         post_result = await crawler.arun(link)
        #         post_html = post_result.markdown
        #         post_soup = BeautifulSoup(post_html, 'html.parser')
                
        #         # Extraction du titre et du contenu avec des sélecteurs adaptés
        #         title_tag = post_soup.find('h1')
        #         content_tag = post_soup.find('div', class_='post-content')
        #         if not title_tag or not content_tag:
        #             continue  # Si les sélecteurs ne correspondent pas, on passe cet article
                
        #         # Conversion du HTML en Markdown
        #         title_md = markdownify.markdownify(str(title_tag), heading_style="ATX")
        #         content_md = markdownify.markdownify(str(content_tag), heading_style="ATX")
                
        #         post = BlogPost(title=title_md, content=content_md, link=link)
        #         posts.append(post)
        #     except Exception as e:
        #         print(f"Error processing {link}: {e}")
    return posts

async def main():
    base_url = "http://www.ngageconsulting.com/blog"
    posts = await fetch_blog_posts(base_url)
    print(posts)
    # Affichage de chaque blog post en format Markdown
    for post in posts:
        print(f"## {post.title}\n")
        print(post.content)
        print(f"\n[Read more]({post.link})\n")
        print("---\n")

if __name__ == '__main__':
    asyncio.run(main())