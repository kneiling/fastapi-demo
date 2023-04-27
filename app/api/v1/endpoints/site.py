from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import dependencies
from app.schemas import site as site_schemas

router = APIRouter()


@router.get("/sites", status_code=status.HTTP_200_OK, response_model=list[site_schemas.Site])
def get_all_sites(db: Session = Depends(dependencies.get_db)):
    sites = crud.site.get_many(db=db, limit=None)
    return sites


@router.get("/sites/{site_id}", status_code=status.HTTP_200_OK, response_model=site_schemas.Site)
def read_site(site_id: int, db: Session = Depends(dependencies.get_db)):
    site = crud.site.get(db=db, id=site_id)
    return site


@router.post("/sites", status_code=status.HTTP_201_CREATED, response_model=site_schemas.Site)
def create_site(site_in: site_schemas.SiteCreate, db: Session = Depends(dependencies.get_db)):
    site = crud.site.create(db=db, obj_in=site_in)
    return site


@router.put("/sites/{site_id}", status_code=status.HTTP_200_OK, response_model=site_schemas.Site)
def update_site(site_id: int, site_in: site_schemas.SiteUpdate, db: Session = Depends(dependencies.get_db)):
    site = crud.site.get(db=db, id=site_id)
    site = crud.site.update(db=db, db_obj=site, obj_in=site_in)
    return site


@router.delete("/sites/{site_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_site(site_id: int, db: Session = Depends(dependencies.get_db)):
    crud.site.delete(db=db, id=site_id)
