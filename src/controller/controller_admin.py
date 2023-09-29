from model.Administradores import Administradores 



class Controller_Admin():
    
    def __init__(self):
        pass

    def inserir_Dividendos(self) -> None:
        return
    
    def atualizar_Dividendos(self):
        return
    
    def deletar_Dividendos(self):
        return   

    def cadastrar_admin(self) -> Administradores:
        nome = input("nome (Novo): ")
        telefone = input("Telefone (Novo): ")
        email = input("E-mail (Novo): ")
        site = input("Site (Novo): ")
        cnpj = input("Cnpj (Novo): ")
        admin = Administradores(nome=nome, telefone=telefone, email=email, site=site, cnpj=cnpj)
        return admin