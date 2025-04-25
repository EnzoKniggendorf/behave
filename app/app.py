from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        senha = request.form.get("senha", "")
        if not email:
            return "Email é obrigatório"
        if not senha:
            return "Senha é obrigatória"
        if "@" not in email:
            return "Email inválido"
        if email == "usuario@teste.com" and senha == "123456":
            return redirect("/dashboard")
        elif email == "usuario@teste.com":
            return "Senha incorreta"
        else:
            return "Email não cadastrado"
    return render_template_string("""
        <form method="post">
            <input name="email" type="text" />
            <input name="senha" type="password" />
            <input type="submit" value="Entrar" />
            <a href="/recuperar">Esqueci minha senha</a>
        </form>
    """)

@app.route("/dashboard")
def dashboard():
    return "Bem-vindo ao dashboard"

@app.route("/logout")
def logout():
    return redirect("/login")

@app.route("/recuperar", methods=["GET", "POST"])
def recuperar():
    if request.method == "POST":
        return "Email de recuperação enviado"
    return render_template_string("""
        <form method="post">
            <input name="email" type="text" />
            <input type="submit" value="Recuperar Senha" />
        </form>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
