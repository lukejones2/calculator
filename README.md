# calculator
Calculator repository

This repo is a calculator implemented in Python. 

By Luke.



### Instructions 

In order to run the streamlit app, you need to run the command: 

```
import pip 
pip.main(['install', 'streamlit', 'pandas', 'numpy'])
```

`streamlit run StreamlitApp.py` 

or if you don't have access to the command line, you can try: 

```
import os
import streamlit.bootstrap
from streamlit import config as _config

_config.set_option("server.headless", True)
streamlit.bootstrap.run(filename, '', args, flag_options={})
```
