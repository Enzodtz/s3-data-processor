from sqlalchemy import Column, Integer, String, SmallInteger, Numeric, Date
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base


class CessaoFundo(Base):
    """
    Tabela criada seguindo o arquivo exemplo .sql,
    com mudança nos campo de documento, de Int para
    String
    """

    __tablename__ = "cessao_fundo"

    id_cessao = Column(Integer, primary_key=True)
    originador = Column(String(250), nullable=False)
    doc_originador = Column(String(50), nullable=False)
    cedente = Column(String(250), nullable=False)
    doc_cedente = Column(String(50), nullable=False)
    ccb = Column(Integer, nullable=False)
    id_externo = Column(Integer, nullable=False)
    cliente = Column(String(250), nullable=False)
    cpf_cnpj = Column(String(50), nullable=False)
    endereco = Column(String(250), nullable=False)
    cep = Column(String(50), nullable=False)
    uf = Column(String(50), nullable=False)
    valor_do_emprestimo = Column(Numeric(10, 2), nullable=False)
    valor_parcela = Column(Numeric(10, 2), nullable=False)
    total_parcelas = Column(Integer, nullable=False)
    parcela = Column(Integer, nullable=False)
    data_de_emissao = Column(Date, nullable=False)
    data_de_vencimento = Column(Date, nullable=False)
    preco_de_aquisicao = Column(Numeric(10, 2), nullable=False)

    def __init__(
        self,
        # id_cessao,
        originador,
        doc_originador,
        cedente,
        doc_cedente,
        ccb,
        id_externo,
        cliente,
        cpf_cnpj,
        endereco,
        cep,
        uf,
        valor_do_emprestimo,
        valor_parcela,
        total_parcelas,
        parcela,
        data_de_emissao,
        data_de_vencimento,
        preco_de_aquisicao,
    ):
        # self.id_cessao = id_cessao
        self.originador = originador
        self.doc_originador = doc_originador
        self.cedente = cedente
        self.doc_cedente = doc_cedente
        self.ccb = ccb
        self.id_externo = id_externo
        self.cliente = cliente
        self.cpf_cnpj = cpf_cnpj
        self.endereco = endereco
        self.cep = cep
        self.uf = uf
        self.valor_do_emprestimo = valor_do_emprestimo
        self.valor_parcela = valor_parcela
        self.total_parcelas = total_parcelas
        self.parcela = parcela
        self.data_de_emissao = data_de_emissao
        self.data_de_vencimento = data_de_vencimento
        self.preco_de_aquisicao = preco_de_aquisicao
