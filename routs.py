from flask import Flask, request, jsonify, render_template
from app.models import db, User, Resume
from app.auth import register_user, login_user
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data['email'], data['password'])

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data['email'], data['password'])

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # In JWT, logout is handled by invalidating tokens on the client side
    return {"message": "Logged out successfully"}

@app.route('/create_resume', methods=['POST'])
@jwt_required()
def create_resume():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_resume = Resume(user_id=user_id, template=data['template'], content=data['content'])
    db.session.add(new_resume)
    db.session.commit()
    return {"message": "Resume created successfully"}

@app.route('/download_resume/<int:resume_id>', methods=['GET'])
@jwt_required()
def download_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    # Generate PDF using WeasyPrint or pdfkit
    html_content = render_template(f"templates/{resume.template}.html", content=resume.content)
    pdf = pdfkit.from_string(html_content, False)
    return pdf, 200, {'Content-Type': 'application/pdf'}
