#export HNSWLIB_NO_NATIVE = 1 <-- command for erroring when running pip install chromadb 
#chromadb is a Vector Database 
import chromadb

chroma_client = chromadb.Client() 

collection = chroma_client.create_collection(name = "my_collection") 

collection.add( 
    #properties listed when result is printed 
    documents = ["my name is max", "my name is not max"], #list of documents from tokenized text
    metadatas = [{"source": "name is true"}, {"source":"name is false"}], #each doc has a source 
    ids = ["id1", "id2"], #each doc has an id 
                         
)

results = collection.query( 
      query_texts=['what is my name?'], 
      n_results=1 #number of results to be displayed                  
) 

print(results) #returns a list of results (dicts) with the distance (smaller distance = more correct to query = favored by LLM) & other properties

