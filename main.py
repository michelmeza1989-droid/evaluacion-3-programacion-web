# Importamos las herramientas necesarias para crear páginas y recibir formularios.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    error = None

    if request.method == "POST":
        try:
            # Convertimos los datos recibidos a números para poder calcular.
            nota1 = float(request.form.get("nota1", ""))
            nota2 = float(request.form.get("nota2", ""))
            nota3 = float(request.form.get("nota3", ""))
            asistencia = float(request.form.get("asistencia", ""))

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
            elif not 0 <= asistencia <= 100:
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = (nota1 + nota2 + nota3) / 3
                # Para aprobar se deben cumplir las dos condiciones.
                if promedio >= 40 and asistencia >= 75:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"
        except ValueError:
            error = "Completa todos los campos con números válidos."

    return render_template("ejercicio1.html", promedio=promedio, estado=estado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombres_mayores = []
    cantidad = None
    error = None

    if request.method == "POST":
        # Quitamos espacios al principio y al final de cada nombre.
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        if not nombre1 or not nombre2 or not nombre3:
            error = "Completa los tres nombres."
        elif (nombre1.casefold() == nombre2.casefold() or
              nombre1.casefold() == nombre3.casefold() or
              nombre2.casefold() == nombre3.casefold()):
            error = "Ingresa tres nombres diferentes."
        else:
            # Primero buscamos la mayor longitud y luego los nombres que la tienen.
            cantidad = len(nombre1)
            if len(nombre2) > cantidad:
                cantidad = len(nombre2)
            if len(nombre3) > cantidad:
                cantidad = len(nombre3)

            if len(nombre1) == cantidad:
                nombres_mayores.append(nombre1)
            if len(nombre2) == cantidad:
                nombres_mayores.append(nombre2)
            if len(nombre3) == cantidad:
                nombres_mayores.append(nombre3)

    return render_template("ejercicio2.html", nombres_mayores=nombres_mayores,
                           cantidad=cantidad, error=error)


# Iniciamos el servidor de desarrollo.
if __name__ == "__main__":
    app.run(debug=True)
