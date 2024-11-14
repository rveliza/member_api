from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/member', methods=['GET'])
def get_member():
    return "This returns all members"

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    return f"This returns one member by id: {member_id}"

@app.route('/member', methods=["POST"])
def add_member():
    return "This adds a new member"

@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return "This updates a member by id"

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return "This deletes a member by id"



if __name__ == "__main__":
    app.run()