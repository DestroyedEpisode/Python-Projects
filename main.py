from flask import Flask, render_template

# chess uft-16 pieces
pieces = {
  'w_king': '\u2654',
  'w_queen': '\u2655',
  'w_rook': '\u2656',
  'w_bishop': '\u2657',
  'w_knight': '\u2658',
  'w_pawn': '\u2659',
  'b_king': '\u265A',
  'b_queen': '\u265B',
  'b_rook': '\u265C',
  'b_bishop': '\u265D',
  'b_knight': '\u265E',
  'b_pawn': '\u265F'
}

def default_board():
  data = []
  row1 = [pieces['w_rook'], pieces['w_knight'], pieces['w_bishop'], pieces['w_king'], pieces['w_queen'], pieces['w_bishop'], pieces['w_knight'], pieces['w_rook']]
  row2 = [pieces['w_pawn'] for _ in range(8)]
  empty = ['' for _ in range(8)]
  row7 = [pieces['b_pawn'] for _ in range(8)]
  row8 = [pieces['b_rook'], pieces['b_knight'], pieces['b_bishop'], pieces['b_king'], pieces['b_queen'], pieces['b_bishop'], pieces['b_knight'], pieces['b_rook']]

  data.append(row1)
  data.append(row2)
  for _ in range(4):
    data.append(empty)
  data.append(row7)
  data.append(row8)
  return data

# Flask part

app = Flask('app')

@app.route('/')
def home():
  layout = default_board()
  return render_template('index.html', data=layout)

app.run(host='0.0.0.0', port=8080)
