from fastapi import Body, FastAPI

app = FastAPI()

PAGES = [
        {"name": "home", "count": 0},
        {"name": "about", "count": 0},
        {"name": "contact", "count": 0}
]

@app.get("/pages")
async def get_all_pages():
    return PAGES

@app.post("/pages")
async def add_page(new_page=Body()):
    PAGES.append(new_page)
    return new_page


@app.put("/pages/{page_name}")
async def update_page(page_name: str, updated_page=Body()):
    for page in PAGES:
        if page["name"] == page_name:
            page["name"] = updated_page["name"]
            page["count"] = updated_page["count"]
            return page

@app.post("/pages/{page_name}/click")
async def add_page_click(page_name: str):
    for page in PAGES:
        if page["name"] == page_name:
            page["count"] += 1
            return page


@app.delete("/pages/{page_name}")
async def delete_page(page_name: str):
    for page in PAGES:
        if page["name"] == page_name:
            PAGES.remove(page)
            return
