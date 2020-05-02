# file_return

> Basic random file returner - created becuase I'm always wanting a random file to test my CNN's and its a pain to keep going back to the folder for file names. I'm just saving my fingers some work.

## Usage

```python

from FileReturn import file_return


fl = file_return(directory="./", include_sub=True, ext=[".jpg",".png"],return_list=False )
random_file =  fl.return_files()

```
