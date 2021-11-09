import pydantic


class StrawberryModel(pydantic.BaseModel):
    pass


class StrawberryORMModel(StrawberryModel):
    class Config(StrawberryModel.Config):
        orm_mode = True


# TODO: Pydantic models go here
