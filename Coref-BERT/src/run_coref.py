import os
import sys
from neuralcoref_resolver import NeuralCoreference

DATA_DIR = "../raw_stories/"
SAVE_DIR = "../processed_stories/"

class CoreferenceResolver:
    def __init__(self,):
        self.coref_resolver = NeuralCoreference()
        
    def read(self, filename):
        with open('../dailymail/stories/'+filename,'r') as f:
            lines = f.readlines()
            print("length:",len(lines))
            s = ''
            content = s.join(lines)
            print(content)
            
    
    def run(self, job):
        self.create_dir()
        count = 0
        with open(f'../deploy/{job}','r') as jf:
            file_list = jf.readlines()
            for i in range(len(file_list)):
                file_list[i]=file_list[i].strip()
        # print(file_list[:10])
        # print(len(file_list))
        # sys.exit(1)
        for file in file_list:
            # if ".story" not in file:
            #     continue
            count += 1
            if file in os.listdir(SAVE_DIR):
                # print("processed",count,file)
                continue
            if count % 50 == 0:
                print("processing", count, file)
            with open(DATA_DIR+file,'r') as f:
                lines = f.readlines()
            raw_content = ""
            boundary_index = -1
            for i, line in enumerate(lines):
                if "@highlight" not in line:
                    raw_content += line
                else:
                    boundary_index = i
                    break
            new_content = self.coref_resolver.coreference_resolver(raw_content)
            for j in range(boundary_index,len(lines)):
                new_content += lines[j]
            with open(SAVE_DIR+file,'w') as f:
                f.write(new_content)
                
                    
            # print("----------------------------------------------------------------------------")
            # if count == 1:
            #     break
    def create_dir(self):
        print(os.listdir('../'))
        if SAVE_DIR[3:-1] not in os.listdir('../'):
            os.mkdir(SAVE_DIR)

if __name__ == '__main__':
    job = sys.argv[1]
    coref_resolver = CoreferenceResolver()
    coref_resolver.run(job)
    # coref_resolver.read('60003cc3ce44012a5480d46251ddb5fa6a8d00ef.story')
    # coref_resolver = NeuralCoreference()
    # print(coref_resolver.coreference_resolver("Jack loves Sandy.\n\nShe is his best friend.\n"))
    
    