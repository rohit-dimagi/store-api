import phonenumbers
from pydantic.validators import strict_str_validator
from pydantic import BaseModel, constr, Field
from uuid import UUID, uuid4


class PhoneNumber(str):
    """Phone Number Pydantic type, using google's phonenumbers"""

    @classmethod
    def __get_validators__(cls):
        yield strict_str_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        # Remove spaces
        v = v.strip().replace(' ', '')

        try:
            pn = phonenumbers.parse(v)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('invalid phone number format')

        return cls(phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164))


class SanitizeQueryParam:
    def sanitize_input(self, param):
        if "," in param:
            param=param.strip('"').split(",")
        else:
            param=[param.strip('"')]
        return param


class Item(BaseModel):
    account_id:constr(regex=r'^[a-zA-Z0-9]+$')
    message_id: UUID = Field(default_factory=uuid4)
    sender_number: PhoneNumber
    receiver_number: PhoneNumber
    class Config:
        orm_mode=True