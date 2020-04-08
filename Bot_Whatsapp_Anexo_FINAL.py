# -*- coding: utf-8 -*-
from selenium import webdriver
import time


class whatsappbot:
    def __init__(self):
        self.mensagem = " Bot Teste - Recebeu manda um legal " # Escreva sua Mensagem
        self.grupos = ["Cíntia Renata IFAN"] #Coloque os nomes dos contatos  separado por virgula
        self.file_name = ('c:\perspectiva.JPEG') #Caminho da Imagem
        option = webdriver.ChromeOptions()
        option.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):

        #<span dir="auto" title="Eu Sozinho" class="_19RFN _1ovWX _F7Vk">Eu Sozinho</span>
        #<span dir="auto" title="Fellipe Dias" class="_19RFN _1ovWX _F7Vk">
        #<div tabindex="-1" class="_3FeAD _1PRhq">
        #<div tabindex="-1" class="_13mgZ"><div tabindex="-1" class="_3FeAD _1PRhq"><div class="wjdTm" style="visibility: visible;">Digite uma mensagem</div><div class="_3u328 copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div></div></div>
        #<span data-icon="send" class="">
        print('Iniciando o WhatsApp Bot')
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            print(f'Buscando o grupo: {grupo}')
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chatbox = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chatbox.click()
            print('Digitando Mensagem')
            time.sleep(1)
            chatbox.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                '//span[@data-icon="send"]')
            time.sleep(3)
            print('Clicando para Enviar')
            botao_enviar.click()
            time.sleep(3)
    #Teste de Envio até linha 41
            print('Anexando arquivo')
            #Clicando no Clip
            anexo = self.driver.find_element_by_xpath(
                '//span[@data-icon="clip"]')
            anexo.click()
            #Clicando no Botão de Anexo
            anexo = self.driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            anexo.send_keys(self.file_name)
            #Clicando no botão de envio
            time.sleep(5)
            botao_image_box = self.driver.find_element_by_xpath(
                '//span[@data-icon="send-light"]')
            botao_image_box.click()
            #Anexo Enviado
            print('Mensagem Enviada com Sucesso')
bot = whatsappbot()
bot.EnviarMensagens()
