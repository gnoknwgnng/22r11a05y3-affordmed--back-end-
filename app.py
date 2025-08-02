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
    {"id": 1,"content" : "22r11a05y3", "title": "akash","deleted": False,"comment": []},
    {"id": 2, "content": "22r11a05u7", "title": "dinesh", "deleted": False,"comment": []},
    {"id": 3, "content": "22r11a05y1", "title": "kruthik","deleted": False, "comment": []},
    {"id": 4, "content": "22r11a05x4", "title": "navneet","deleted": False, "comment": []},
    {"id": 5, "content": "22r11a05y4", "title": "suresh","deleted": False, "comment": []},
    {"id": 6, "content": "22r11a05y5", "title": "karthik","deleted": False, "comment": []},
    {"id": 7, "content": "22r11a05y6", "title": "vedhas","deleted": False, "comment": []},
    {"id": 8, "content": "22r11a05y7", "title": "tarun","deleted": False, "comment": []},
    {"id": 9, "content": "22r11a05y8", "title": "ramesh","deleted": False, "comment": []},
    {"id": 10, "content": "22r11a05y9", "title": "varun","deleted": False, "comment": []}
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


@app.get("/blogs/{id}/comment")
def get_comments(id: int):
    if 0 <= id-1 < len(blogs_json):
        print("Fetching comments for blog", id)
        print("the comment is",blogs_json[id-1]["comment"])
        return {"message": "Comments for blog", "blog_id": id, "comment": blogs_json[id-1]["comment"]}
    else:
        return {"error": "Blog not found"}
    
@app.post("/blogs/{id}/comment")   
def add_comment(id: int, comment: str):
    if 0 <= id-1 < len(blogs_json):
        blogs_json[id-1]["comment"].append(comment)
        print("Comment added successfully",blogs_json[id-1]["comment"])
        return {"message": "Comment added successfully", "blog_id": id, "comment": comment}
    else:
        return {"error": "Blog not found"}
    
@app.delete("/blogs/{id}/comment")
def delete_comment(id: int, comment: str):
    if 0 <= id-1 < len(blogs_json):
        if comment in blogs_json[id-1]["comment"]:
            blogs_json[id-1]["comment"].remove(comment)
            print("Comment deleted successfully",blogs_json[id-1]["comment"])
            return {"message": "Comment deleted successfully", "blog_id": id, "comment": comment}
        else:
            print("Comment not found")
            return {"error": "Comment not found"}
    else:
        return {"error": "Blog not found"}
    
