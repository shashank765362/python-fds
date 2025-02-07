from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(email, password):
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {"message": "User registered successfully"}

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}
    return {"error": "Invalid credentials"}, 401
