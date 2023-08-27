import sys
import torch
from BERT import predict_text


if __name__ == "__main__":

    user_input = sys.argv[1]

    # print(user_input)
    
    # Run ML code here
    arr = predict_text(user_input)

    print(arr)