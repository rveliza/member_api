from flask import Flask, g, request, jsonify
from database import get_db

app = Flask(__name__)
app.config['DEBUG'] = True

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/member', methods=['GET'])
def get_member():
    db = get_db()
    members_cur = db.execute("SELECT * FROM members")
    all_members = members_cur.fetchall()
    return_values = []

    for member in all_members:
        member_dict = {}
        member_dict['id'] = member['id']
        member_dict['name'] = member['name']
        member_dict['email'] = member['email']
        member_dict['level'] = member['level']
        return_values.append(member_dict)
    
    return jsonify({'members': return_values})

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):

    db = get_db()
    member_cur = db.execute('SELECT * FROM members WHERE id = ?', [member_id])
    member = member_cur.fetchone()

    member_id = member['id']
    member_name = member['name']
    member_email = member['email']
    member_level = member['level']

    return jsonify({'member': {'id': member_id, 'name': member_name, 'email': member_email, 'level': member_level}})

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

    # Return json object from db
    member_cur = db.execute('SELECT id, name, email, level FROM members WHERE name = ?', [name])
    new_member = member_cur.fetchone()

    db_id = new_member['id']
    db_name = new_member['name']
    db_email = new_member['email']
    db_level = new_member['level']

    return jsonify({'member': {'id': db_id, 'name': db_name, 'email': db_email, 'level': db_level}})

@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return "This updates a member by id"

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return "This deletes a member by id"



if __name__ == "__main__":
    app.run()