from pydantic import UUID4, BaseModel, field_validator, Field

class LanguageDelete(BaseModel):
    id: UUID4 = Field(...)