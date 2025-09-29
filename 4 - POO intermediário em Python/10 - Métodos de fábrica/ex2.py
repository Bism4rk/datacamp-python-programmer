class DataPipeline:
  def _get_database(self, provider):
    if provider == "Postgres":
      return Postgres() # type: ignore
    elif provider == "Redshift":
      return Redshift() # type: ignore

  def extract_data(self, provider, query):
    database = self._get_database(provider)
    dataset = database.query_data(query) # type: ignore
    print(f"Extracted dataset from {provider} database")
    return dataset

# Create an ETL DataPipeline, query using Redshift
items_pipeline = DataPipeline()
items_pipeline.extract_data("Redshift", "SELECT * FROM items;")

# Now, switch the pipeline to Postgres
items_pipeline.extract_data("Postgres", "SELECT * FROM items")

# Finally, create an etl_pipeline with Redshift
etl_pipeline = DataPipeline()
etl_pipeline.extract_data("Redshift", "SELECT * FROM sales;")

'''
O código acima demonstra como implementar métodos de fábrica em Python usando classes abstratas e herança. Ele define uma interface comum para diferentes tipos de clientes (membros de recompensas e novos clientes) e utiliza um método de fábrica para instanciar o tipo correto de cliente com base na entrada fornecida. A classe Checkout gerencia o processo de pagamento, delegando a responsabilidade ao objeto cliente apropriado.
'''
