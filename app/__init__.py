from fastapi import FastAPI, status, HTTPException, Depends, Request
from sqlalchemy.orm import Session 
from sqlalchemy.exc import IntegrityError


from database import get_db, engine
import models
from schema import SignupRequest, SignupResponse

app = FastAPI()


users = []

models.Base.metadata.create_all(bind=engine)


@app.get('/')
def home():
    return "This is a home page"


@app.get('/echo')
def home(data:str):
    return f"This is {data}"


@app.get('/about')
def about(name: str, surname: str):
    return f"This is a about page for {name} {surname}"


@app.get('/signup', status_code=201)
def create_user(username: str, password: str, email: str, db: Session = Depends(get_db)):
    new_user = models.User(username=username, password=password, email=email)
    db.add(new_user)
    db.commit()

    print("********************************")
    print(users)
    print("********************************")
    return "User created"


@app.post('/new_signup', status_code=201, response_model=SignupResponse)
async def create_user(id: str, data:SignupRequest , db: Session = Depends(get_db)):

    print("id ------->",id)
    username = data.username
    password = data.password
    email = data.email

    new_user = models.User(username=username, password=password, email=email)
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User already exists")

    print("********************************")
    print(users)
    print("********************************")
    return {"username": username, "password": password, "email": email, "id":1}



@app.get('/login')
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and user.password == password:
        return "Login successful"
    return "Login failed, Username or password incorrect"


@app.get('/delete-profile', status_code=status.HTTP_200_OK)
def delete_profile(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and user.password == password:
        db.delete(user)
        db.commit()
        return "Profile deleted successfully"

    raise HTTPException(status.HTTP_404_NOT_FOUND ,detail="Username or password incorrect")


@app.get('/update-password')
def delete_profile(username: str, old_password: str, new_password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and user.password == old_password:
        user.password = new_password
        db.commit()
        return "Profile updated successfully"

        
    raise HTTPException(status.HTTP_404_NOT_FOUND ,detail="Username or password incorrect")

# http://127.0.0.1:8000/signup?username=shubham&email=shubham@gmail.com&password=xyz5678
# http://127.0.0.1:8000/signup?username=amanupadhyay&email=aman@gmail.com&password=abcd1234