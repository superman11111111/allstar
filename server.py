from astar import astar

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/astar', methods=['POST'])
def handle_astar():
  import json
  r = json.loads(request.data)
  m = r['m']
  sN = r['start']
  eN = r['end']
  print(f"y={len(m)}, x={len(m[0])}")
  route = astar(m, sN, eN)
  print(route)
  path = []
  for n in route:
    print((len(m[0])+1)*n.x)
    path.append((len(m[0])+1)*n.x+n.y-n.x)
  return json.dumps({'path': path})
  return str((m, sN)) 
  return hello_world()
  

@app.route('/')
def hello_world():
  dim = (10, 20)
  grid = []
  for i in range(dim[0]):
    b = []
    for j in range(dim[1]):
      b.append(f"<div id={i}{j}></div>")
    grid.append("".join(b))
    #print(grid)
  grid = "\n".join(grid)
  # print(grid)
  return render_template('index.html') 

if __name__ == "__main__":
  app.run(debug=True)
