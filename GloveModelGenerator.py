import os
import pandas as pd
import gensim
from mecab_dealer import Doc2Words

def generate_word_list_file(lower_bound):
    dir = "/home/masaomi/sentence_classification/original_data/"
    xl_files = ["PharmacyReportPub-0.xlsx", "PharmacyReportPub-1.xlsx", "PharmacyReportPub-2.xlsx"]
    d2w = Doc2Words(dir,xl_files)
    arranged_word_dict, deleted_word_list, decomposition_dict, core_word_dict = d2w.key_arrangement(lower_bound=lower_bound)
    output_word_list = d2w.translate_all_to_list(deleted_word_list, decomposition_dict)
    with open("/home/masaomi/translated_word_list.txt","w") as f:
        for wl in output_word_list:
            _wl = [ w+" " for w in wl]
            f.writelines(_wl)
            f.write("\n")
    print("Generated!")

def generate_vocabulary_file(lower_bound):
    vocab_count = "/home/masaomi/glove/build/vocab_count"
    min_word_count = "-min-count %s"%lower_bound
    verbose = "-verbose 2"
    input_file = "/home/masaomi/translated_word_list.txt"
    output_file = "/home/masaomi/vocab.txt"
    command_list = [vocab_count, min_word_count, verbose, "<", input_file, ">", output_file]
    command = " ".join(command_list)
    os.system(command)

def generate_coocur_mat_file():
    cooccur = "/home/masaomi/glove/build/cooccur"
    memory = "-memory 8"
    input_file = "/home/masaomi/translated_word_list.txt"
    vocab_file = "-vocab-file /home/masaomi/vocab.txt"
    window_size = "-window-size 10"
    output_file = "/home/masaomi/cooccurrence.txt"
    command_list = [cooccur, memory, vocab_file, window_size, "<", input_file, ">", output_file]
    command = " ".join(command_list)
    os.system(command)

def shuffle():
    shuffle = "/home/masaomi/glove/build/shuffle"
    memory = "-memory 8"
    verbose = "-verbose 2"
    output_file = "/home/masaomi/cooccurrence_shuffle"
    command_list = [shuffle, memory, verbose, "<", "/home/masaomi/cooccurrence.txt", ">", output_file]
    command = " ".join(command_list)
    os.system(command)

def apply_glove(dim, iter=10):
    glove = "/home/masaomi/glove/build/glove"
    save_file = "-save-file /home/masaomi/vectors"
    threads = "-threads 3" #2
    input_file = "-input-file /home/masaomi/cooccurrence_shuffle"
    x_max = "-x-max 100"
    iter_num = "-iter %s"%iter
    vector_size = "-vector-size %s"%dim
    binary = "-binary 2"
    vocab_file = "-vocab-file /home/masaomi/vocab.txt"
    command_list = [glove, save_file, threads, input_file, x_max, iter_num, vector_size, binary, vocab_file]
    command = " ".join(command_list)
    os.system(command)

def generate_gensim_file():
    vectors = pd.read_csv('/home/masaomi/vectors.txt', delimiter=' ', index_col=0, header=None)
    with open('/home/masaomi/vectors.txt', 'r') as original, open('/home/masaomi/gensim_vectors.txt', 'w') as transformed:
        vocab_count = vectors.shape[0]
        size = vectors.shape[1]
        transformed.write(f'{vocab_count} {size}\n')
        transformed.write(original.read())

def get_glove_vector():
    glove_vectors = gensim.models.KeyedVectors.load_word2vec_format('/home/masaomi/gensim_vectors.txt', binary=False)
    return glove_vectors, glove_vectors.vector_size

if __name__ == "__main__":
    lower_bound = 5 #10
    dim = 100
    generate_word_list_file(lower_bound)
    generate_vocabulary_file(lower_bound)
    generate_coocur_mat_file()
    shuffle()
    apply_glove(dim, iter=100)
    generate_gensim_file()
    gv, size = get_glove_vector()
    print("--------------\n")
    print(gv.most_similar("ロキソプロフェン"))
    print("--------------\n")
    #print(gv.most_similar("酸化マグネシウム300mg")
