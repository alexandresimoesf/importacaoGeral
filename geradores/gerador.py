class Gerador:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Gerar : {', '.join(self.parts)}", end="")