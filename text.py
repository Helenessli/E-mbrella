import sys
import torch
from BERT import predict_text


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python text.py <input>")
    # else:

    user_input = sys.argv[1]
    
    # Run ML code here
    arr = predict_text(user_input)

    print(str(arr[0])+' '+str(arr[1]))
                    
            