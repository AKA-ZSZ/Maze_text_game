from models.maze import Maze
from flask import Flask,request,render_template


app = Flask(__name__)
maze=Maze()

@app.route('/', methods=['GET'])
def default():
    """ homepage """
    return render_template('index.html',scores=sorted(maze.scores,key=lambda x: (x['score']),reverse=True))



@app.route('/api/list')
def list_all_scores():
    return {"scores": maze.scores}

@app.route('/api/new', methods=["PUT"])
def add_new_score():
    data = request.get_json()
    if data is None:
        return "Empty data.", 400

    if len(data) != 2:
        return "Invalid keys.", 400

    if type(data["name"]) != str or type(data["score"]) != float:
        return "Invalid data provided.", 400
    
    score = [data["name"], data["score"]]
    
    maze.add_score(score)

    return "", 204

if __name__ == "__main__":
    app.run(debug=True)