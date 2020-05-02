# file_return

### Basic random file returner 
>
> Useful when testing image transforms etc. I find I am constantly trying to gather
> a random images while working with CNN's
> I've made made this to help me tidy up my code.

## Usage

```python

from FileReturn import file_return


fl = file_return(directory="./", include_sub=True, prefix_ext=[".jpg",".png"],return_list=False )
random_file =  fl.return_files()

```

## For more examples see below

[Jupyter Examples](./examples.ipynb)
