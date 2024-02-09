from fastapi import FastAPI;
from typing import Optional;
from pydantic import BaseModel;
import uvicorn;

app = FastAPI();

@app.get("/blog")
def index(limit:int =10, published:bool=True,sort: Optional[str] =None):
    if published:
        return {'data':f"{limit} published blogs from the db"};
    elif sort!=None:
        return {'data':f"{limit} blogs from the db sorted by {sort}"};
    else:
        return {'data':f"{limit} blogs is listed"};

@app.get("/blog/{id}")
def blog(id:int):
    return {'blog':id};


@app.get("/blog/{id}/comments")
def comments(id:int):
    if(id==1):
        return {"comment":"This is my comment"};
    
    else:
        return {"comment":"no cmoment found"};



class Blog(BaseModel):
    title:str;
    body:str;
    published:Optional[bool];

@app.post("/blog")
def create_blog(blog:Blog):
    return f"Created a new blog with a title  as: {blog.title}";

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000);
