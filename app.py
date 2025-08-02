from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI()

class Blogs(BaseModel):
    id: int


class Blogs(BaseModel):
    id: int
    title: str = ""
    content: str = ""

blogs_json=[
    {"id": 1,"content" : "22r11a05y3", "title": "First Post","deleted": False},
    {"id": 2, "content": "22r11a05u7", "title": "Second Post", "deleted": False},
    {"id": 3, "content": "22r11a05y1", "title": "Third Post","deleted": False},
]


@app.get("/blogs")
def blogs():
    return blogs_json

@app.get("/blogs/{id}")

def blog(id: int):
    return blogs_json[id-1] if 0 <= id-1 < len(blogs_json) else {"error": "Blog not found"}

@app.get("/blogs/{id}")
def blogs(id: int,limit:int = 10,offset:int = 0):
   print(limit, offset)
   return blogs_json[id-1] if 0 <= id-1 < len(blogs_json) else {"error": "Blog not found"}

@app.post("/blogs")
def create_blog(blog: Blogs):
     print(blog)
     return {"message": "Blog created successfully", "blog": blog}

@app.put("/blogs/{id}")
def update_blog(id: int, blog: Blogs):
    if 0 <= id-1 < len(blogs_json):
        blogs_json[id-1] = blog.dict()
        print(blog)
        print(blogs_json[id-1])
        return {"message": "Blog updated successfully", "blog": blog}
    else:
        return {"error": "Blog not found"}
    
@app.patch("/blogs/{id}")
def patch_blog(id: int, blog: Blogs):
    if 0 <= id-1 < len(blogs_json):
        blogs_json[id-1].update(blog.dict())
        print(blog)
        print(blogs_json[id-1])
        return {"message": "Blog patched successfully", "blog": blogs_json[id-1]}
    else:
        return {"error": "Blog not found"}
    
@app.delete("/blogs/{id}")
def delete_blog(deleted: bool, id: int):
    if 0 <= id-1 < len(blogs_json):
        blogs_json[id-1]["deleted"] = True
        print(blogs_json[id-1])
        return {"message": "Blog deleted successfully", "blog": blogs_json[id-1]}
    else:
        return {"error": "Blog not found"}