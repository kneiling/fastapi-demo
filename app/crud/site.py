from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.site import Site
from app.schemas import site as site_schemas


class CRUDSite(CRUDBase[Site, site_schemas.SiteCreate, site_schemas.SiteUpdate]):
    def create(self, db: Session, obj_in: site_schemas.SiteCreate) -> Site:
        site = Site(
            name = obj_in.name,
            multiplier = obj_in.multiplier,
        )

        db.add(site)
        db.commit()
        db.refresh(site)

        return site


site = CRUDSite(Site)
