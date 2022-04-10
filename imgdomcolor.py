from collections import Counter
import cv2
from sklearn.cluster import KMeans
import argparse
import cv2
import numpy as np
import pandas as pd
df=pd.read_csv("Dataset1_clean.csv")
def get_dominant_color(image, k=4, image_processing_size=None):

    # resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size, interpolation=cv2.INTER_AREA)

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster the pixels and assign labels
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image)

    # count labels to find most popular
    label_counts = Counter(labels)

    # subset out most popular centroid
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

    return list(dominant_color)


# construct the argument parser and parse the arguments

# read in image of interest
for i in range(len(df)):
  bgr_image = cv2.imread("/content/drive/My Drive/d1_img/"+df.iloc[i,15]+".jpg")
# convert to HSV; this is a better representation of how we see color
  hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

  # extract dominant color
  # (aka the centroid of the most popular k means cluster)
  dom_color = get_dominant_color(hsv_image, k=6)

  # create a square showing dominant color of equal size to input image
  dom_color_hsv = np.full(bgr_image.shape, dom_color, dtype='uint8')
  # convert to bgr color space for display
  dom_color_bgr = cv2.cvtColor(dom_color_hsv, cv2.COLOR_HSV2BGR)

  # concat input image and dom color square side by side for display
  output_image = np.hstack((bgr_image, dom_color_bgr))

  # show results to screen
  #cv2_imshow( output_image)
  #print(dom_color_hsv[1][1])
  df2 = df2.append( pd.Series([df.iloc[i,15],dom_color_hsv[1][1]],index=df2.columns),ignore_index=True)
  df2.to_csv("color.csv", mode='a', header=False, index=False)
