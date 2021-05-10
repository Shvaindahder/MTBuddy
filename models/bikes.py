from app import db


class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(32), unique=True, nullable=False)
    regions = db.relationship("Regions", backref="city", cascade="delete")


class Regions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), nullable=False)
    region = db.Column(db.String(64), nullable=False, unique=True)
    shops = db.relationship("Shops", backref="region", cascade="delete")


class Shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)
    name = db.Column(db.String(64))
    shop_url = db.Column(db.String(128), nullable=True)
    
