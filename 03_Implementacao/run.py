from final_report_app.final_report import create_app

#Chama a função create_app para se conseguir
#criar a aplicação Flask com as configurações
#necessárias
app = create_app()

#Se o ficheiro estiver a ser executado diretamente
if __name__ == "__main__":
    #Inicia o servidor de desenvolvimento Flask
    #com o modo de debug ativo
    app.run(host="0.0.0.0", port=5000, debug=True)