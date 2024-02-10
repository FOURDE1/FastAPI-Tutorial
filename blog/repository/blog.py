from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status



def create(request:schemas.Blog,db:Session):
    new_blog =models.Blog(title=request.title,body=request.body,creator_id=1);
    db.add(new_blog);
    db.commit();
    db.refresh(new_blog);
    return new_blog;

def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id);
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog {id} is not found");

    blog.delete(synchronize_session=False);
    db.commit();
    return {"Deleted"};