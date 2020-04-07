from flask import Flask, render_template, abort
from lxml import etree
app = Flask(__name__)

@app.route('/')
def inicio():
	return render_template("inicio.html")

@app.route('/potencia/<int:base>/<int:exponente>')
def calc_potencia (base,exponente):
	if exponente > 0:
		resultado = base**exponente
	elif exponente == 0:
		resultado = 1
	elif exponente < 0:
        	resultado = 1/(base**abs(exponente))
	return render_template("potencia.html",base=base,exp=exponente,resultado=resultado)

@app.route('/cuenta/<palabra>/<letra>')
def cuenta_letra (palabra,letra):
	if len(palabra) > 1:
		cont = palabra.count(letra)
	else:
		abort(404)
	return render_template("contar.html",palabra=palabra,letra=letra,apariciones=cont)

@app.route('/libro/<int:codigo>')
def info_libros (codigo):
	doc = etree.parse('libros.xml')
	if str(codigo) in doc.xpath('/biblioteca/libro/codigo/text()'):
		autor=doc.xpath('/biblioteca/libro[codigo/text()="%s"]/autor/text()' %codigo)[0]
		titulo=doc.xpath('/biblioteca/libro[codigo/text()="%s"]/titulo/text()' %codigo)[0]
	else:
		abort(404)
	return render_template("libros.html",titulo=titulo,autor=autor)

app.run(debug=True)
