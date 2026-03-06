from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form.get("nome")
        whatsapp = request.form.get("whatsapp")
        mensagem = f"Olá, quero garantir minha declaração de Imposto de Renda 2026 pelo valor promocional de R$80. Nome: {nome}"
        url = f"https://wa.me/{whatsapp}?text={mensagem.replace(' ', '%20')}"
        return redirect(url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    