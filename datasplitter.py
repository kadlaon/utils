import sys

def split_dataset(input_file_path, domain, language):
    domain = domain
    language = language
    train_file_path = domain +"."+ language +"."+"train.bpe" 
    test_file_path = domain +"."+ language +"."+"test.bpe" 
    dev_file_path = domain + "."+language +"."+ "dev.bpe"

    with open(input_file_path, "r", encoding="utf-8") as input_file, \
         open(train_file_path, "w", encoding="utf-8") as train_file, \
         open(test_file_path, "w", encoding="utf-8") as test_file, \
         open(dev_file_path, "w", encoding="utf-8") as dev_file:

        dataset = input_file.readlines()
        dataset_len = len(dataset)
        train_len = int(dataset_len * 0.80)
        test_dev_len = int(dataset_len * 0.10)

        for i, each_sentence in enumerate(dataset):
            if 0 < i < train_len:
                train_file.write(each_sentence)
            elif train_len < i < train_len + test_dev_len:
                dev_file.write(each_sentence)
            else:
                test_file.write(each_sentence)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    domain = sys.argv[2]
    language = sys.argv[3]

    split_dataset(input_file_path, domain, language)
    print("Dataset split successfully!")