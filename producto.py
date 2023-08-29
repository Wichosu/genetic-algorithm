class Producto: 
    def __init__(self, nombre: str, calorias: int, peso: float) -> None:
        self.nombre = nombre
        self.calorias = calorias
        self.peso = peso

    def __str__(self) -> str:
        return f"{self.nombre}, {self.calorias}, {self.peso}"