from fastapi import APIRouter,status,Depends,Response,HTTPException
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(
    prefix="/blog", # we can write this for each endpoint or include it like this
    tags=['Blogs'] # we can write this  for each endpoint  or include it like this

)


get_db=database.get_db;


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.create(request,db);


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
   return blog.destroy(id,db);

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db)):
   blog= db.query(models.Blog).filter(models.Blog.id==id);
   if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog {id} is not found");
   
   blog.update({"title":request.title,"body":request.body},synchronize_session=False );
   db.commit();
   return {"updated"};

@router.get("/",response_model=list[schemas.ShowBlog])
def get_all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all();
    return blogs;


@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def show(id:int,response:Response,db:Session=Depends(get_db) ,):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first();
    if not blog:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog {id} is not found");
        # response.status_code = status.HTTP_404_NOT_FOUND;
        # return {"detail":"Blog not found"};

    return blog;