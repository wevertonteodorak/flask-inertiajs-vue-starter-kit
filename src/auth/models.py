from flask_login import UserMixin
from src.app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id) if user_id else None
    
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def create_user(name, email, password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def update_user(name=None, email=None, password=None, original_email=None):
        print('updating user..')
        user = User.get_user_by_email(email=original_email) 
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            if password:
                user.password = generate_password_hash(password)
            db.session.commit()
            return user
        print('nao achou:', user)
        return None
    
    @staticmethod
    def delete_user(user_id):
        user = User.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def user_exists(email):
        return User.query.filter_by(email=email).first() is not None
    
    def check_password(self, password):
        if not self.password:
            return False
        return check_password_hash(self.password, password)