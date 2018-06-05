'''
Created on 16 de abr de 2018

@author: gdiamante
'''
from behave import *
from selenium import webdriver   
import time

@given("estar com a pagina do Google aberta")
def stepEntrarPaginaPrincipal(context):
    
    #acessando a pagina desejada
    
    context.web = webdriver.Chrome()
    context.web.get("https://www.google.com/")
    
@when("ser redirecionado para a pagina inicial")
def stepValidaPaginaPrincipal(context):
    
    #confirmando a url atual da pagina acessada
    
    currenturl = context.web.current_url
    print("------- A url desta pagina e " + currenturl + " -------")
    time.sleep(1)
    
@then("validar titulo da pagina")
def stepValidaTituloPagina(context):
    
    
    #verificando o titulo da pagina

    print("------- O titulo desta pagina e " + context.web.title + " -------")
    
    assert(context.web.title == "Google"),"------- Erro. Titulo da pagina nao validado -------"
    print("------- Titulo da pagina validado com sucesso -------")
 

    
    
    
  

    

    
    
    
    