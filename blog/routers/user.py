from fastapi import APIRouter,status,Depends,Response
from .. import schemas,database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user", # we can write this for each endpoint or include it like this
    tags=['Users'] # we can write this  for each endpoint  or include it like this 

)


get_db=database.get_db;

@router.post('/',response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.UserBase,db:Session=Depends(get_db)):
  return user.create(request,db);

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int ,db:Session=Depends(get_db)):
   return user.get(id,db);