class Ordem:
    def __init__(self, id, status, orcamento, data, recibo, feedback, produto):
        self.id = id
        self.status = status
        self.orcamento = orcamento
        self.data = data
        self.recibo = recibo
        self.feedback = feedback
        self.produto = produto

        def consultarOrdem(self):
            ordem = f"""
                id: {self.id}
                data: {self.data}
                produto: {self.produto}
            """

            return ordem

        def getStatus(self):
            return self.status

        def getOrcamento(self):
            return self.orcamento

        def comprovante(self):
            return self.recibo
        