__author__ = 'Vardhaman'
import sys, math
index ={}
doc_len_dict = {}
index_term_freq = {}
num_of_docs = 0
avg_doc_len = 0
total_doc_len = 0
final_index = {}
#bm_25_dict = {}

#calculate the doc length of each doc 
def cal_doc_len():
    global num_of_docs
    global total_doc_len
    global avg_doc_len
    f = open("./doc_length.txt",'r')
    for line in f.readlines():
        num_of_docs += 1
        word = line.split()
        doc_len_dict[word[0]] = int(word[1])
        total_doc_len += int(word[1])
    #print(doc_len_dict)
    print("Doc length",total_doc_len)
    print("Num of docs",num_of_docs)
    avg_doc_len = float(total_doc_len)/num_of_docs
    print("Average len",float(total_doc_len)/num_of_docs)

#retrieving word and its frequency from the index
def read_index_term_fre():
    f = open("./key_freq.txt",'r')
    for line in f.readlines():
        word = line.split()
        index_term_freq[word[0]] = int(word[1])
    #print(index_term_freq)

def read_final_index(file):
    f= open(file,'r')
    for line in f.readlines():
        temp_dict = {}
        word = line.split()
        w = word[1].split(':')
        for d in w:
            c = d.split(',')
            temp_dict[c[0]] = int(c[1])
        final_index[word[0]] = temp_dict
    #print(final_index)

#parameters for computation of bm25    
k1 = 1.2
k2 = 100
b = 0.75
ri = 0.0
R = 0.0

#compute the bm25 score
def compute_bm_25(q,qf,bm_25_dict):
    if final_index.has_key(q):
        #print(final_index[q])
        for doc_id,df in final_index[q].iteritems():
            #print (doc_id,df)
            avdl = float((doc_len_dict[doc_id]) / avg_doc_len)
            k = k1*((1-b)+b*avdl)
            #tmp = float(0.75*doc_len_dict[doc_id]) / avg_doc_len
            #kk = 1.2 * (0.25 + tmp)
            #score = float((num_of_docs - index_term_freq[q] + 0.5)* (2.2 * df * 101 *qf))/ ((index_term_freq[q]+0.5)*(kk+df)*(100*qf))
            score = (math.log(float(num_of_docs - index_term_freq[q] + 0.5)/(index_term_freq[q]+0.5)))*(((k1+1)*df)/(k+df))*(((k2+1)*qf)/(k2+qf))
            if bm_25_dict.has_key(doc_id):
                bm_25_dict[doc_id] += score
            else:
                bm_25_dict[doc_id] = score
    #print(bm_25_dict)
    score = 0
 
#read queries from query file 
def read_queries(queryfile,num):
    #global bm_25_dict
    bm_25_dict = {}
    f= open(queryfile,'r')
    f1 = open("./results.eval",'w')
    qid = 1
    for line in f.readlines():
        bm_25_dict = {}
        query_dict = {}
        word = line.split()
        for w in word:
            #print(w)
            if query_dict.has_key(w):
                query_dict[w] += 1
            else:
                query_dict[w] = 1
        print(query_dict)
        for k,v in query_dict.items():
            #print (k,v)
            compute_bm_25(k,v,bm_25_dict)
        Freq = sorted(bm_25_dict, key=bm_25_dict.get, reverse=True)
        for i in range(int(num)):
            f1.write(str(qid)+" "+"Q0"+" "+str(Freq[i])+" "+str(i+1)+" "+str(bm_25_dict.get(Freq[i]))+" "+"metpally.v")
            f1.write("\n")
            #print(Freq[i], bm_25_dict.get(Freq[i]))
        qid = qid+1
        
if __name__ == "__main__":
    if len(sys.argv) == 4:
        newfile = sys.argv[1]
        queryfile = sys.argv[2]
        num = sys.argv[3]
        read_final_index(newfile)
        cal_doc_len()
        read_index_term_fre()
        read_queries(queryfile,num)
