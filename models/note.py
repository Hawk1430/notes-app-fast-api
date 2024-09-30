from pydantic import  BaseModel



class CreateNoteModel(BaseModel):
    title: str
    desc: str
    # important: bool = False