from  flask import Blueprint
auth=Blueprint('auth',__name__)
from app.api import account,message,note