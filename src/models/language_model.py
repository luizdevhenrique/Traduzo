from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def to_dict(self):
        return {
          "name": self.data["name"],
          "acronym": self.data["acronym"]
        }

    def list_dicts():
        languages = LanguageModel._collection.find()
        return [LanguageModel(d).to_dict() for d in languages]
