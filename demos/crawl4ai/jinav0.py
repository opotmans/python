def scrap_jina_ai(url:str) -> str:
    response  = requests.get("https://r.jina.ai/" + url)
    return response.text

if __name__ == "__main__":
    print(scrap_jina_ai("www.ngageconsulting.com/blog"))
