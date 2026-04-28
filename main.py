from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/name/{name}")
def greet_name(name:str):
    return {"message": f"Hello, {name}!"}

@app.get("/rechne/{zahl}")
def rechne (zahl: float):
result = (zahl +2)*3
return {"message": f"Das Ergebnis von {zahl} ist {ergebnis}"}
#zwei weiter @app.get "dinger bauen wo man einen wert rein bekommt und diesen Weiterverarbeite (z.B Uhrzeit.... und die nächste volle stunde ist wenn 12.40 eingegeben wird dass dann 13 Uhr raus kommt. Und dann z.B Zahl die eingegeben wird plus 2 und dann mal 3)"