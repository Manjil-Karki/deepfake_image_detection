from PIL import Image
import pandas as pd
import os
import tqdm

df = pd.read_json("done.json")
df = df.T.to_numpy()

images = os.listdir(r"Train")
fake_count = 0
real_count = 0


for i in tqdm.tqdm(range(df.shape[0])):
    cat = df[i][0]
    bbox = df[i][1]
    path = df[i][2]

    img_name = path.split('/')[-1]
    
    if img_name not in images:
        continue
    

    img = Image.open(path)


    im = img.crop(bbox)
    
    # im = im.resize((128, 128))

    if cat == 1:
        im.save(fr"F:\Minor project\Codes\data\fake\fake_{fake_count}.jpg")
        fake_count += 1
    else:
        im.save(fr"F:\Minor project\Codes\data\real\real_{real_count}.jpg")
        real_count += 1
    

# # im.save("./new.jpg")
# img.show()