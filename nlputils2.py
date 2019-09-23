from fastai.basics import *
import re
import urllib.request

    
def get_wiki_download(path,lang):
    name = f'{lang}wiki'
    xml_fn = f"{lang}wiki-latest-pages-articles.xml"
    zip_fn = f"{xml_fn}.bz2"    
    
    if (path/zip_fn).exists():
        print(f"{path/zip_fn} already exists; not downloading")
        return
    else:
        print("downloading...")
        download_url(f'https://dumps.wikimedia.org/{name}/latest/{zip_fn}', path/zip_fn)

def get_wiki_unzip(path,lang):
    name = f'{lang}wiki'
    xml_fn = f"{lang}wiki-latest-pages-articles.xml"
    zip_fn = f"{xml_fn}.bz2"
    
    if (path/xml_fn).exists():
        print(f"{path/xml_fn} already exists; not unzip")
        return    
    else:
        print("unzipping...")
        bunzip(path/zip_fn)
    
def get_wiki_extract(path,lang):
    name = f'{lang}wiki'
    xml_fn = f"{lang}wiki-latest-pages-articles.xml"
    zip_fn = f"{xml_fn}.bz2"

    with working_directory(path):
        
        # get updated wikiextractor folder from albertvillanova, not attardi
        if not (path/'wikiextractor').exists(): os.system('git clone https://github.com/attardi/wikiextractor.git')
#         if not (path/'wikiextractor').exists(): os.system('git clone https://github.com/albertvillanova/wikiextractor.git')
        
        # if you cloned the wikiextractor folder from attardi, get the platform-independent WikiExtractor.py file with this code
        file_path = path/'wikiextractor/WikiExtractor.py'
        os.unlink(file_path) # delete existing file
        url = 'https://raw.githubusercontent.com/piegu/fastai-projects/master/WikiExtractor.py' # updated file url
        urllib.request.urlretrieve(url, file_path) # get updated file
        
        if (path/'wikiextractor/WikiExtractor.py').exists(): 
            print("extracting...")
            os.system("python wikiextractor/WikiExtractor.py --processes 4 --no_templates " +
                f"--min_text_length 1800 --filter_disambig_pages --log_file log -b 100G -q {xml_fn}")
            shutil.move(str(path/'text/AA/wiki_00'), str(path/name))
            shutil.rmtree(path/'text')
        else:
            print(f"the file {path}\wikiextractor\WikiExtractor.py does not exist")

def split_wiki2(path,lang):
    dest = path/'docs'
    name = f'{lang}wiki'
    if dest.exists():
        print(f"{dest} already exists; not splitting")
        return dest

    dest.mkdir(exist_ok=True, parents=True)
    title_re = re.compile(rf'<doc id="\d+" url="https://{lang}.wikipedia.org/wiki\?curid=\d+" title="([^"]+)">')
#     re_punc = re.compile("([\"'().,;:/_?!—\-*])") # replace ponctuation
    re_punc = re.compile("([^a-zA-Z0-9])") # replace ponctuation in title

#     lines = (path/name).open()
    lines = (path/name).open(encoding="utf8") # platform independent with utf8
    
    f=None

    for i,l in enumerate(lines):
        if i%100000 == 0: print(i)
        if l.startswith('<doc id="'):
#             title = title_re.findall(l)[0].replace('/','_')
            title = title_re.findall(l)[0]
            title = re_punc.sub(r"_", title)
            if len(title)>150: continue
            if title == "Com8": continue # exception
            if f: f.close()
#             f = (dest/f'{title}.txt').open('w')
            f = (dest/f'{title}.txt').open('w', encoding="utf8") # platform independent with utf8
        else: f.write(l)
    f.close()
    return dest


def clean_files(path,folder):

    dest = path/folder
    doc_re = re.compile(rf'([\w\W]*)<\/doc>') # delete </doc>
               
    for i,l in enumerate(dest.ls()):
        # open file and get content without first line which is the title
        f = l.open('r+', encoding="utf-8")
        f.readline()
        text = f.read()
        # get content without </doc> and delete empty line and whitespaces at the head and tail
        text = doc_re.findall(text)[0].strip()
        # delete file content
        f.seek(0)
        f.truncate()
        # write modificated text in file
        f.write(text)
        f.close()

def get_num_tokens(dest):
    
    # Getting an idea of the number of words
    files = dest.ls()
    num_tokens = 0

    for i,l in enumerate(files):
        f = l.open('r', encoding="utf-8")
        words = f.read()
        num_tokens += len(words.split())
        f.close()
        
    num_files = i+1
    
    return num_files, num_tokens

# Create a corpus of about obj_token words in a corpus_'obj_token' folder
def get_corpus(dest, path, num_tokens, obj_tokens=int(1e8)):
    
    num_tokens_article_min = 100
    
    if num_tokens >= obj_tokens:
    
        # number of tokens by text
        files = dest.ls()
        sizes = []
        list_idx = []

        for i,f in enumerate(files):
            sizes.append(os.path.getsize(f))

        total_size = np.array(sizes).astype(np.int64).sum()
        tokens_by_file = np.array(sizes)*(num_tokens/total_size)

        # Sorted list of texts ids 
        num = 0

        tokens_by_file_sorted = np.argsort(tokens_by_file)

        #for i,idx in enumerate(tokens_by_file_sorted[:-len(tokens_by_file_sorted)-1:-1]):
        for i,idx in enumerate(tokens_by_file_sorted):
            if tokens_by_file[idx] >= num_tokens_article_min:
                num += tokens_by_file[idx]
                list_idx.append(i)
            if num >= obj_tokens: break

        articles_idxs = tokens_by_file_sorted[list_idx]

        # creation of the corpus folder
        folder = 'corpus_'+str(int(obj_tokens))
        path_corpus = path/folder
        path_corpus.mkdir(exist_ok=True, parents=True)

        # copy text files to corpus folder
        for idx in articles_idxs:
            file = files[idx]
            shutil.copy(str(file), str(path_corpus))

        print(f'files copied to the new corpus folder: {path/folder}')

        return path_corpus
    
    else:
        
        print('As there are less than 100 000 000 tokens in the initial corpus, we use it.')
        
        return dest
