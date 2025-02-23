import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import AIMessage
async def main():
    # Configure the browser
    browser_cfg = BrowserConfig(
        headless=False,
        viewport_width=1280,
        viewport_height=720,
        text_mode=True
    )

    # Configure the run
    run_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        session_id="my_session",
        css_selector="main.article",
        excluded_tags=["script", "style"],
        exclude_external_links=True,
        screenshot=True,
        stream=True
    )

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun(
            url="https://www.ngageconsulting.com/blog",
            config=run_cfg
        )
        if result.success:
            print("Final cleaned_html length:", len(result.cleaned_html))
            if result.screenshot:
                print("Screenshot captured (base64, length):", len(result.screenshot))
        else:
            print("Crawl failed:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())