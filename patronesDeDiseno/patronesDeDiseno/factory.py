import json

from abc import ABC, abstractmethod
from pathlib import Path
from os import path

from pydantic import BaseModel  # pip instal pydantic

class Config(ABC):
    conf_type: str
    
    @property
    @abstractmethod
    def conf_type(cls):
        """Force inheritant classes to have conf_type class variable."""
        pass
    
    @classmethod
    def get_allowed_types(cls) -> dict[str, 'Config']:
        """Builds a dict of supported conf types extensions.

        Returns:
            dict[str, Conf]: dict with type and allowed conf object
        """
        subclasses = cls.__subclasses__()
        search_attribute = "conf_type"
        allowed_types: dict[str, 'Config'] = {}
        for subclass in subclasses:
            if hasattr(subclass, search_attribute):
                allowed_types[getattr(subclass, search_attribute)] = subclass()
        return allowed_types
    
    def __init__(self, conf_path: None | str):
        abs_path: str | None = path.abspath(conf_path) if conf_path is not None else None
        self._path: str | None = abs_path
      
    @abstractmethod  
    def ingest_conf(self, schema: None | BaseModel = None):
        """Ingests and makes every field of the conf file an object attribute.
        Args:
            schema (None | BaseModel, optional): A pydantic class to validate that the content of a config file follows a given schema. 
            Defaults to None.

        Returns:
            Conf: The object with every field in the JSON file as an attribute.
        """
        pass
    
    @property
    def path(self) -> str | None:
        """Absolute path of the passed conf file

        Returns:
            str | None: Returns the absolute path of the passed conf file, 
            none if the conf file path its not set.
        """
        return self._path


    @path.setter
    def path(self, new_path: str) -> None:
        """Sets a new absolute path for a Conf object"

        Args:
            new_path (str): The new absolute path where the conf file is located.

        Raises:
            ValueError: In case the new path given doesn't exist.
        """
        if not Path(new_path).exists():
            raise ValueError(f"The given path {new_path} doesn't exist.")
        self._path = path.abspath(new_path)

       
class JsonConfig(Config):
    conf_type = ".json"
    def __init__(self, conf_path: None | str = None) -> 'JsonConfig':
        super().__init__(conf_path)
    
    #@override
    def ingest_conf(self, schema = None):
        if self._path is None: 
            raise ValueError("The path is not set yet!")
        with open(self._path, "r") as conf:
            json_content: dict = json.load(conf)
        if schema is not None:
            if not isinstance(schema, type):
                 raise ValueError("Please pass the schema class, not an instance of the class.")
            schema(**json_content)  # validate that the JSON has the schema specified
            
        for key, value in json_content.items():
            setattr(self, key.lower(), value)
        return self
       
        
class ConfigFactory:
    @staticmethod
    def get_conf(conf_path: str, schema: None | BaseModel = None) -> Config:
        """Returns the most appropiate conf object for the filepath given, 
        parses the content of the file to a given schema if needed.

        Args:
            conf_path (str): The absolute or relative path to the config file. Defaults to None.
            schema (None | BaseModel, optional): The schema to validate the content of the conf file. Defaults to None.

        Returns:
            Conf: The implemented conf object that best fits to the file extension of conf file.
        """
        def init_conf_obj(conf_obj: Config, abs_path: str, schema: None | BaseModel) -> Config:
            """Initializates conf object 

            Args:
                conf_obj (Conf): The implemented conf object that best fits to the file extension of conf file.
                abs_path (str): The absolute path to the config file. Defaults to None.
                schema (None | BaseModel): _description_

            Returns:
                Conf: The initialized conf object.
            """
            conf_obj.path = abs_path
            conf_obj.ingest_conf(schema)
            return conf_obj
        
        abs_path = path.abspath(conf_path)  # absolute path of conf file
        if not Path(abs_path).exists(): raise ValueError(f"The path {conf_path} doesn't exist.")
        
        _, file_extension = path.splitext(conf_path)
        types: dict[str, Config] = Config.get_allowed_types()
        conf_obj: Config = types.get(file_extension)
        
        if conf_obj is None: raise ValueError(f"{file_extension} type is not yet supported!")
        return init_conf_obj(conf_obj, abs_path, schema)


if __name__ == "__main__":
    conf: Config = ConfigFactory.get_conf(r"conf\conf.json")
    print(conf.ip)