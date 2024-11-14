from flask import Flask, g, request
from database import get_db

app = Flask(__name__)
app.config['DEBUG'] = True

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/member', methods=['GET'])
def get_member():
    return "This returns all members"

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    return f"This returns one member by id: {member_id}"

@app.route('/member', methods=["POST"])
def add_member():
    new_member_data = request.get_json()
    # print(new_member_data)
    # {'name': 'Reyner', 'email': 'reyner@reynerveliz.com', 'level': 'Platinum'}
    name = new_member_data['name']
    email = new_member_data['email']
    level = new_member_data['level']

    db = get_db()
    db.execute('INSERT into members (name, email, level) VALUES (?,?,?)', [name, email, level])
    db.commit()

    return f"Name: {name}, Email: {email}, Level: {level}"

@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return "This updates a member by id"

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return "This deletes a member by id"



if __name__ == "__main__":
    app.run()