from pydantic import BaseModel
class GiftVoucher(BaseModel):
    voucher_id:str
    amount:float
    recipient:str