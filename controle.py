from PyQt5 import  uic,QtWidgets
import sqlite3

def funcao_principal():
    telaprincipal.label.setText("")
    usuario = telaprincipal.lineEdit.text()
    senha = telaprincipal.lineEdit_2.text()

    if usuario == "funcionario" and senha == "1234" :
        telaprincipal.close()
        segundatela.show()
def cadastrar():
    segundatela.close()
    terceiratela.show()

def salvar():
    nome = terceiratela.lineEdit.text()
    idade =terceiratela.lineEdit_2.text()
    sexo = terceiratela.lineEdit_3.text()
    telefone =terceiratela.lineEdit_4.text()
    try:
        banco = sqlite3.connect('bancodados.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados(nome text, idade text, sexo text, telefone text)")
        cursor.execute("INSERT INTO dados VALUES('"+nome+"','"+idade+"','"+sexo+"','"+telefone+"')")
        banco.commit()
        banco.close()
    
        print("Cadasto concluido!")


    except sqlite3.Error as erro :
        print("Erro ao enserir os dados",erro)


app=QtWidgets.QApplication([])
telaprincipal=uic.loadUi("telaprincipal.ui")
segundatela =uic.loadUi("segundatela.ui")
terceiratela =uic.loadUi("terceiratela.ui")
telaprincipal.pushButton.clicked.connect(funcao_principal)
segundatela.pushButton_2.clicked.connect(cadastrar)
terceiratela.pushButton.clicked.connect(salvar)


telaprincipal.show()
app.exec()

