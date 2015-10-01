author__ = 'Vardhaman'
import sys
key_freq ={}
index = {}
final_index = {}
doc_index_list = []
#doc_index = {}
count = 0

#build the index
def build_index(doc_index_list):
    #global final_index
    #print(doc_index_list)
    for i, val in enumerate(doc_index_list):
        #print(val)
        for k,v in val.items():
            #print(i,k,val[k])
            temp = str(i+1)+","+str(v)
            #print(temp)
            #print(i+1,len(val))
            if final_index.has_key(k):
                final_index[k] = final_index[k]+":"+temp
            else:
                final_index[k]= temp
    print_final_dict(final_index)


def print_final_dict(final_index):
    fh = open("./indexer.out",'w')
    for k in final_index.keys():
        linestr = k +" "+str(final_index[k])
        fh.write(linestr)
        #fh.write(k)
        #fh.write(final_index[k])
        fh.write("\n")
        #print (k,final_index[k])
    f = open("./doc_length.txt",'w')
    #num_of_docs = 0
    #doc_len = 0
    for i, val in enumerate(doc_index_list):
        #num_of_docs += 1
        value = 0
        for k,v in val.items():
            value = value+v
        f.write(str(i+1)+" "+str(value))
        f.write("\n")
        #doc_len += value
    #print("Doc length",doc_len)
    #print("Num of docs",num_of_docs)
    #print("Average len",float(doc_len)/num_of_docs)

#method to build each document and then words and their frequency
def build_docf(newfile):
    input = open(newfile, 'r')
    doc_index = {}
    for line in input.readlines():
        if line.startswith('#'):
            if len(doc_index) >0:
                doc_index_list.append(doc_index)
            doc_index = {}
            '''if len(doc_index) >0:
                doc_index_list.append(doc_index)'''
        else:
            word = line.split()
            for w in word:
                #print (w)
                if doc_index.has_key(w):
                    #index[w] += 1
                    doc_index[w] += 1
                else:
                    #index[w] = 1
                    doc_index[w] = 1
    doc_index_list.append(doc_index)
    build_index(doc_index_list)

#build index frequency
def build_index_freq(newfile):
    input = open(newfile, 'r')
    flag = 0
    local_dict = {}
    for line in input.readlines():
        if line.startswith('#'):
            for k in local_dict.keys():
                if key_freq.has_key(k):
                    key_freq[k] += 1
                else:
                    key_freq[k] = 1
            local_dict = {}
        else:
            word = line.split()
            for w in word:
                #print (w)
                if local_dict.has_key(w):
                    co = 0#do nothing
                else:
                    #index[w] = 1
                    local_dict[w] = 1
    fh = open("./key_freq.txt",'w')
    tmp = 0
    for k in key_freq.keys():
        #tmp += key_freq[k]
        fh.write(k+" "+str(key_freq[k]))
        fh.write("\n")
    #print("Total doc length is",sum(key_freq.values()))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        newfile = sys.argv[1]
        build_docf(newfile)
        build_index_freq(newfile)
