from jina import Executor, requests
import time
import requests as req
from bs4 import BeautifulSoup

class BlogScraper(Executor):
    @requests
    def scrap_all_blogs(self, docs, **kwargs):
        base_url = "https://rjina.ai/https://www.ngageconsulting.com/blog"
        headers = {
        "Authorization": "Bearer jina_9e08dce6fb7c40078cf02154af6ba150y3GF8Z88r2lu3gqirensw6Z5SRQo",
        "X-Retain-Images": "none",
        "X-With-Links-Summary": "true"
        }
        response = req.get(base_url,headers=headers)
        print(response.status_code)
               
        # if response.status_code == 200:
        #     soup = BeautifulSoup(response.text, 'html.parser')
        #     blog_links = [a['href'] for a in soup.find_all('a', href=True) if '/blog/' in a['href']]
        #     print (blog_links)
        #     blog_contents = []
        #     for link in blog_links:
        #         blog_response = req.get(link)
        #         if blog_response.status_code == 200:
        #             blog_soup = BeautifulSoup(blog_response.text, 'html.parser')
        #             blog_contents.append(blog_soup.get_text())
        #             time.sleep(2)
            
        #     docs[0].text = "\n\n".join(blog_contents)
        # else:
        #     docs[0].text = "Failed to retrieve blogs."
        # print(blog_links)


if __name__ == "__main__":
    from jina import Flow, Document
    
    flow = Flow().add(uses=BlogScraper)

    with flow:
        result = flow.post(on="/scrap", inputs=Document(), return_results=True)
        print(result[0].docs[0].text)
