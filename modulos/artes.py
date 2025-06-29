from time import sleep

#TODAS AS FUNÇÕES DOCUMENTADAS

def art_pata():
    """Imprime na tela uma arte de uma pata, uma releitura em ASCII da logo original do P.A.T.A.S."""
    pata = '''
    ­
             %%%%     %%%%%%          
            %%%%%%%  %%%%%%%%       
            %%%%%%%  %%%%%%%%       
            %%%%%%%  %%%%%%%%      
            %%%%%%% %%%%%%%%%       
    %%%%%%  %%%%%%   %%%%%%%  %%%% 
    %%%%%%%%  %%%     %%%%% %%%%%%%%
    %%%%%%%%%               %%%%%%%%
    %%%%%%%%%  %%%%%%%%%%  %%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
     %%%%%%%%%%%%%%%%%%%%%%%%%%  
          %%%%%%%%%%%%%%%%%%      
          %%%%%%%%%%%%%%%%%%%%     
          %%%%%%%%%%%%%%%%%%%%%     
          %%%%%%%%%%%%%%%%%%%%%    
          %%%%%%%%%%%%%%%%%%%%%    
           %%%%%%%    %%%%%%%%     
    ­
    '''.strip().split('\n') #Remove espaços em branco no início e no final de cada linha e divide a string em várias linhas
    for linha in pata:
        print(linha.center(100)) # Centraliza a arte da pata na tela
def art_nomepatas():
    """Imprime na tela uma arte "PATAS', uma releitura em ASCII da logo original do P.A.T.A.S."""
    nomepatas = '''
    ­                         
        @@@@@@@@@@@@@@@@        @@@@@@       @@@@@@@@@@@@@@@@@@            @@@@@@              @@@@@@@@@@           
        @@@@@@@@@@@@@@@     @@@@@@@@@@       @@@@@@@@@@@@@@@@@@        @@@@@@@@@@            @@@@@@@@@@@@@            
        @@@@@@@@@@@@@@@     @@@@@@@@@@        @@@@@@@@@@@@@@@@@        @@@@@@@@@@            @@@@@@@@@@@@             
        @@@@@   @@@@@@      @@@@@@@@@@       @@@@@@@@@@@@@@@@@@       @@@@@@@@@@@          @@@@@@@@@              
        @@@@@  @@@@@@@      @@@@@@@@@@       @@@  @@@@@@@ @@@@        @@@@@@@@@@          @@@@@@@              
        @@@@@@@@@@@@        @@@@@@@@@@            @@@@@@@             @@@@@@@@@@          @@@@@@@@@@@@@@            
        @@@@@@@@@@         @@@@  @@@@@@@          @@@@@@@             @@@@ @@@@@@@@       @@@@@@@@@@@@@@            
        @@@@@@@@           @@@@ @@@@@@@@          @@@@@@@            @@@@ @@@@@@@@              @@@@@@@@            
        @@@@@@            @@@@@@@@@@@             @@@@@@@            @@@@@@@@@@@                  @@@@@@@           
        @@@@@             @@@@@@@@@@@@            @@@@@@@           @@@@@@@@@@@@                 @@@@@@@           
        @@@@@            @@@@@@@@@@@@@@           @@@@@@@           @@@@@@@@@@@@@@          @@@@@@@@@@@@           
        @@@@@@          @@@@@@@  @@@@@@@          @@@@@@@          @@@@@@@  @@@@@@@           @@@@@@@@@            
        @@@@@@          @@@@@@    @@@@@           @@@@@@@         @@@@@@    @@@@@             @@@@@@@                                                                                      
    ­
    '''.strip().split('\n') #Remove espaços em branco no início e no final de cada linha e divide a string em várias linhas
    for linha in nomepatas:
        print(linha.center(100)) # Centraliza a arte do nome "PATAS" na tela
def conjunto(pata = str(''), nome= str('')):
    """Imprime na tela uma arte de uma *pata* e o nome "PATAS', 
    uma releitura em ASCII da logo original do P.A.T.A.S,
    juntamente com algumas divisões usando -="""
    print('-='*60)
    print('-='*60)
    print('-='*60)
    art_pata() # Chama a função que imprime a arte da pata
    sleep(1)
    art_nomepatas() # Chama a função que imprime a arte do nome "PATAS"
    print('-='*60)
    print('-='*60)
    print('-='*60)
    print()
    sleep(1)