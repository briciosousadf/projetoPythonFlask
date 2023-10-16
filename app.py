from flask import Flask, render_template

app =  Flask(__name__)

frase = "Esta frase está no back end!"

produto = {
    "id" : 123,
    "nome" : "Caixa JBL Pro Sound ",
    "descricao" : "Potente JBL Original Pro Sound Quatro drivers e dois radiadores de graves JBL oferecem um som simplesmente potente e imersivo, com graves profundos e nitidez nos detalhes. Você vai ser levado pela música onde quer que esteja.",
    "valor" : 699.00,
    "imagem" : "https://app.vitrinedigital.net/imperiocell/16835-large_default/caixa-de-som-xtreme-3-jbl-original.jpg"
}

produtos = {
    1 : {
            "id" : 123,
            "nome" : "Caixa JBL Pro Sound ",
            "descricao" : "Potente JBL Original Pro Sound Quatro drivers e dois radiadores de graves JBL oferecem um som simplesmente potente e imersivo, com graves profundos e nitidez nos detalhes. Você vai ser levado pela música onde quer que esteja.",
            "valor" : 1450.00,
            "imagem" : "https://app.vitrinedigital.net/imperiocell/16835-large_default/caixa-de-som-xtreme-3-jbl-original.jpg"
        },
    2 : {
            "id" : 456,
            "nome" : "Echco Dot 5a geração ",
            "descricao" : "SUAS MÚSICAS E CONTEÚDOS FAVORITOS - Reproduza músicas e podcasts do Amazon Music, Apple Music, Spotify, entre outros, ou por Bluetooth em todos os ambientes da sua casa.",
            "valor" : 390.00,
            "imagem" : "https://cdn.dooca.store/85562/products/1-17_640x640.png?v=1674052216&webp=0"
        },
    3 : {
            "id" : 789,
            "nome" : "Mini Projetor ",
            "descricao" : "Mini Projetor Portatil 5G Wifi 6 Bluetooth 5.0 Android 11, Projetor 4K 1080P Full HD Suporte 8000 Lumens, Projetor Led Auto de Correcção Trapezóide Horizontal, 180°Girável Projector para Telefónico (US Plug)",
            "valor" : 399.00,
            "imagem" : "https://m.media-amazon.com/images/I/5133wKaOqSL._AC_SX679_.jpg"
        },
    4 : {
            "id" : 147,
            "nome" : "Relogio Watch 4 Pro ",
            "descricao" : "2023 nfc relógio inteligente masculino gt4 pro 390*390 tela hd freqüência cardíaca bluetooth chamada ip67 à prova dip67 água smartwatch para huawei xiaomi + caixa",
            "valor" : 699.00,
            "imagem" : "https://http2.mlstatic.com/D_NQ_NP_2X_667148-MLB71699834010_092023-F.webp"
        },
    5 : {
            "id" : 258,
            "nome" : "Beats Pro ",
            "descricao" : "Fone de ouvido supra-auricular Beats Pro - Prateado",
            "valor" : 2300.00,
            "imagem" : "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MH6P2?wid=1144&hei=1144&fmt=jpeg&qlt=95&.v=0"
        },
    6 : {
            "id" : 369,
            "nome" : "Roteador WDS ",
            "descricao" : "Roteador, WDS Bridge TP-Link Archer C5400X V1 preto e vermelho 100V/240V",
            "valor" : 2600.00,
            "imagem" : "https://http2.mlstatic.com/D_NQ_NP_2X_970204-MLA48124463122_112021-F.webp"
        }

}

@app.route("/")
def exibir_mensagem():
    return render_template("exemplo.html", texto = frase)

@app.route("/produto")
def exibe_produto():
    return render_template("produto.html", **produto)

@app.route("/produtos")
def exibe_produtos():
    return render_template("lista_produtos.html", produtos=produtos)
app.run(debug=True)