from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
import pandas as pd
from pandas import json_normalize
from tqdm import tqdm

# Specify the endpoint
sparql = SPARQLWrapper("https://dati.cultura.gov.it/sparql")

sparql.setQuery("""
PREFIX arco-arco: <https://w3id.org/arco/ontology/arco/>

SELECT ?entity ?id
WHERE {
  ?entity a arco-arco:HistoricOrArtisticProperty ;
          arco-arco:uniqueIdentifier ?id .
}
limit 3000
"""
)

# Set the return format to JSON
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# Normalize the JSON results into a pandas DataFrame
results_df = pd.json_normalize(results['results']['bindings'])
art_props = results_df[['entity.value', 'id.value']]
print(len(art_props))


# Extract the list of entity URLs
links = art_props["entity.value"].to_list()


# Initialize empty lists to store the information
total_desc = []
total_cov = []
total_mat = []
total_date = []
total_title = []

# Iterate over the links (URLs of cultural objects)
for url in tqdm(links):
    # Create an RDF graph
    g = Graph()
    # Parse RDF data from the URL
    g.parse(url, format="turtle")  # Assuming the data is in Turtle format, change format if needed
    # Define the SPARQL query to select all predicates and objects
    query = """
        SELECT ?predicate ?object
        WHERE {
            ?subject ?predicate ?object
        }
        """
    # Initialize empty lists to store the selected information for the current URL
    selected_desc = []
    selected_cov = []
    selected_mat = []
    selected_date = []
    selected_title = []
    selected_type = []
    # match against the predicates
    lista_token = ["https://w3id.org/arco/ontology/core/description", "http://purl.org/dc/elements/1.1/coverage",
                   "http://data.cochrane.org/ontologies/pico/materialAndTechnique", "http://purl.org/dc/elements/1.1/date",
                   "http://purl.org/dc/elements/1.1/title", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"]
    results = g.query(query)
    for row in results:
        #print(row)

        predicate = str(row[0])
        #print(predicate)
        obj = str(row[1])
        # Check if the predicate matches any of the tokens in the lista_token list
        for token in lista_token:
            if token in predicate and predicate.endswith("description"):
                selected_desc.append(obj)
            if token in predicate and predicate.endswith("coverage"):
                selected_cov.append(obj)
            if token in predicate and predicate.endswith("materialAndTechnique"):
                selected_mat.append(obj)
            if token in predicate and predicate.endswith("date"):
                selected_date.append(obj)
            if token in predicate and predicate.endswith("title"):
                selected_title.append(obj)
            else:
                pass
        #break
    #print(selected)
    total_desc.append(selected_desc)
    total_cov.append(selected_cov)
    total_mat.append(selected_mat)
    total_date.append(selected_date)
    total_title.append(selected_title)


# Create dataframe
data = {"nome":total_title, "data": total_date, "materiale":total_mat, "locus":total_cov, "description":total_desc}
artistic_objs_df = pd.DataFrame(data)
