# file_return

> Basic random file returner - becuase I'm always wanting a random file to test my CNN's and its a pain to keep going back to the folder for file names or re-writing the same code when I need it. Just saving myself some finger time.


## Installation 

in terminal 

```
git clone https://github.com/lewis-morris/file_return/
cd file_return
pip install -e .

```

## Usage

```python

from FileReturn import file_return


fl = file_return(directory="./", include_sub=True, prefix_ext=[".jpg",".png"], return_list=False )
random_file =  fl.return_files()

```

## For more info check the example jupyter notebook

[Jupyter examples](./examples.ipynb)
