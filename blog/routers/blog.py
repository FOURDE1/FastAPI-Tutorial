from fastapi import APIRouter,status,Depends,Response,HTTPException
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(
    prefix="/blog", # we can write this for each endpoint or include it like this
    tags=['Blogs'] # we can write this  for each endpoint  or include it like this

)


get_db=database.get_db;


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db);


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.destroy(id,db);

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db);

@router.get("/",response_model=list[schemas.ShowBlog])
def get_all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.get_all(db);


@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def show(id:int,response:Response,db:Session=Depends(get_db) ,current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db,response);