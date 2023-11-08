# Scrapper Dados Jovem Nerd 

Pipeline de dados para coleta de dados do site Jovem Nerd com integração com Airflow. Foi criada uma DAG que envia os dados coletados da API para o Kaggle. Link para o dataset no Kaggle [Jovem Nerd Podcasts](https://www.kaggle.com/datasets/victorstein/nerdcast).


### Build do docker

```bash
docker build -t scrapper-jovem-nerd .
```

### Execução do docker

Executar sem enviar o `data.csv` para o Kaggle
```bash
docker run -it -v /your/path/here:/home/var/data -p 8080:8080 scrapper_jovem_nerd
```

Para enviar o dataset para o Kaggle as variáveis de ambiente devem ser configuradas
```bash
docker run -it -v /your/path/here:/home/var/data -e "KAGGLE_USERNAME=KAGGLE_USERNAME" -e "KAGGLE_KEY=KAGGLE_KEY" -p 8080:8080 scrapper_jovem_nerd
```

O airflow vai suber na porta 8080, para acessar o painel basta acessar `http://localhost:8080/`. A DAG criada tem o nome de `jovem_nerd_dag`. A DAG cria um arquivo chamado `data.csv` na pasta `/home/var/data` do container. 