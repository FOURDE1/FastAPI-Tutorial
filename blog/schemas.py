from pydantic import BaseModel;
from sqlalchemy.orm import relationship;
from typing import List,Optional

class UserBase(BaseModel):
    name:str;
    email:str;
    password:str;

class User(BaseModel):
    name:str;
    email:str;  

class BlogBase(BaseModel):
    title:str;
    body:str;
    
class Blog(BlogBase):
   
    class Config():
        from_attributes = True;

class ShowUser(BaseModel):
    name:str;
    email:str;
    blogs:List[Blog] =[];
    class Config():
        from_attributes = True;





class ShowBlog(BaseModel):
    title:str;
    body:str;
    creator:User;
   
    class Config():
        from_attributes = True;




class Login(BaseModel):
    username:str;
    password:str;


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    