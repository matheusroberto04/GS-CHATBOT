from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/templates/index.html')
def index():
    return render_template('index.html')

@app.route('/processa_envio', methods=['POST'])
def processa_envio():
    if 'imagem' in request.files:
        imagem = request.files['imagem']
        nome = request.form['nome']
        comentario = request.form['comentario']

        # Lógica para processar a imagem e os dados (armazenamento, processamento, etc.)
        # Neste exemplo, apenas imprime informações na console.
        print(f'Nome: {nome}')
        print(f'Comentário: {comentario}')
        print(f'Arquivo de imagem: {imagem.filename}')

        return 'Envio bem-sucedido!'
    
    return 'Erro no envio. Certifique-se de incluir uma imagem.'

if __name__ == '__main__':
    app.run(debug=True)

