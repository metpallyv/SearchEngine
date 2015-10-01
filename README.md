# SearchEngine for TREC collection of documents
The goal of this project is to implement a simple Search Engine using various retrieval models using tf-idf and BM25

Goal of this project is to build a simple Search Engine in python for TREC documents using various retrieval models like tf-idf,BM25 and compare the performance for various retreival models using the following:

1. Read in the tokenized and stemmed document collection provided in the file tccorpus.txt. This is an early standard collection of abstracts from the Communications of the ACM.
    Format for Tokenized Document Collection in tccorpus.txt is:
        A # followed by a document ID
        Lines below the document ID line contain stemmed words from the document.
        For example:

        # 1
        this is a tokenzied line for document 1
        this is also a line of document 1
        # 2
        from here lines for document 2 begin
        ...
        ...
        # 3
        ...

2. Build a simple inverted indexer that reads the corpus and writes the index. 
                You should invoke it with :  indexer tccorpus.txt index.out

3. Implement the BM25 ranking algorithm and write a program to provide a ranked list of documents for a file with one or more queries. You should pass parameters for the index file, the query file, and the maximum number of document results, and return documents on the standard output, 
                like so:  bm25 index.out queries.txt 100 > results.eval
  
4. For BM25 Ranking use the following:

      1. Retrieve all inverted lists corresponding to terms in a query.
      2. Compute BM25 scores for documents in the lists.
      3. Make a score list for documents in the inverted lists.
      4. Accumulate scores for each term in a query on the score list.
      5. Assume that no relevance information is available.
      6. For parameters, use k1=1.2, b=0.75, k2=100.
      7. Sort the documents by the BM25 scores.

5. Output the top 100 document IDs and their BM25 scores for each test query 
                according to the following format: query_id Q0 doc_id rank BM25_score system_name

6. Use the following Test Queries:

        Query ID	Query Text
        1	        portabl oper system
        2	        code optim for space effici
        3	        parallel algorithm
        4	        distribut comput structur and algorithm
        5	        appli stochast process
        6	        perform evalu and model of comput system
        7	        parallel processor in inform retriev
