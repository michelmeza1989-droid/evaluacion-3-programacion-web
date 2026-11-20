# Evaluación 3 - Programación Web

Aplicación sencilla en Flask con dos ejercicios: cálculo de notas y asistencia, y comparación de nombres.

## Ejecución

Desde la carpeta del proyecto en Linux, activa el entorno virtual existente y ejecuta:

```bash
source .venv/bin/activate
python main.py
```

Abre `http://127.0.0.1:5000` en el navegador. Para detener el servidor, presiona `Ctrl+C` en la terminal. Si se utiliza otro equipo, se necesita Python y Flask instalados en su propio entorno virtual (`pip install -r requirements.txt`).

Las notas se ingresan en escala de 10 a 70. Se aprueba con promedio igual o superior a 40 y asistencia igual o superior a 75 %. El promedio se muestra con dos decimales; el estado se calcula con el valor completo.

Al compartir el proyecto, incluye `main.py`, `requirements.txt`, las carpetas `templates` y `static`, y este archivo. No incluyas `.venv`, archivos `.env` ni datos sensibles.
