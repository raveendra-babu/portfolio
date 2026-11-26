from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import Form, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Contact

from fastapi import Depends, Form




app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/css',StaticFiles(directory='css'),name='css')
Base.metadata.create_all(bind=engine)
@app.get("/")
def home(request: Request):

    theme = request.cookies.get("theme", "dark")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "theme": theme
        }
    )
    
    
@app.get("/change-theme/{theme}")
def change_theme(theme: str):

    if theme not in ["light", "dark"]:
        theme = "dark"

    response = RedirectResponse(
        url="/",
        status_code=303
    )

    response.set_cookie(
        key="theme",
        value=theme,
        max_age=60 * 60 * 24 * 30,
    )

    return response
    
# @app.post("/contact")
# def submit_contact(
#     name: str = Form(...),
#     email: str = Form(...),
#     mobile: str = Form(...),
#     message: str = Form(...),
#     db: Session = Depends(get_db)
# ):
#     contact = Contact(
#         name=name,
#         email=email,
#         mobile=mobile,
#         message=message
#     )

#     db.add(contact)
#     db.commit()

#     return RedirectResponse(
#         url="/#contact",
#         status_code=303
#     )
    

