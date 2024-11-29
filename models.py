#models.py
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel
import json

class Location(BaseModel):
 id: Optional[UUID] = uuid4()
 label: str
 score: float
 housenumber: int
 street : str
 postcode : str
 city : str
 citycode : str
 type : str
 name : str
 lon : float
 lat : float
 context : str
 importance : float 
 def afficher(self): 
      print("id : "+"\t"+ str(self.id))     
      print("adresse : "+"\t"+ self.label)    
      print("position lon,lat : "+"\t"+ str(self.lon)+"\t"+str(self.lat))   
 def json_reponse(self):
      return json.dumps({'score':self.score,'label':self.label,'housenumber':self.housenumber,
            'street':self.street,'postcode':self.postcode,'citycode':self.citycode,
            'city':self.city,'lon':self.lon,'lat':self.lat,'type':self.type,
                'name':self.name,'context':self.context,'importance':self.importance})    
 def get_latlon(self):
      return(self.lat,self.lon)   
