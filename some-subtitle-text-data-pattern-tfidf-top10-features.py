#!/usr/bin/env python2.7

# sudo apt-get install python-pattern
# setting python2.7 version for debian/ubuntu
# sudo update-alternatives --config python

def get_model_from_documents(path='./*/*.txt'):
    '''return model from given txt files'''
    import codecs
    import glob
    from pattern.vector import Document, Model, TFIDF

    documents=[]
    files=glob.glob('./*/*.*')
    for file in files:
        f=codecs.open(file, 'r')
        data=f.read()
        document=Document(data)
        documents.append(document)

    model = Model(documents=documents, weight=TFIDF)
    return documents, model

def save_top_ten(documents):
    '''save top10 for each document using documents.id'''
    import codecs
    from pattern.vector import Document, Model, TFIDF
#    for document in documents:
#        print(document.vector)

    output=codecs.open('top10-terms-by-document-id.csv', 'w')
    for document in documents:
        keywords=document.keywords()
        for key, value in keywords:
            output.write(u'"' + value + u'"\t"' + str(key) + u'"\t"' + document.id + '"\n')
    output.close()

def save_features(model):
    '''saving features for a given model'''
    import codecs
    from pattern.vector import Document, Model, TFIDF
    output=codecs.open('features.csv', 'w')
    for feature in model.features:
        output.write(u'"' + feature + u'"\n')
    output.close()

def main():
    documents, model = get_model_from_documents('../*/*.*') # including '*.url' files too 
    save_top_ten(documents)
    save_features(model)

if __name__ == "__main__":
    # execute only if run as a script
    main()
