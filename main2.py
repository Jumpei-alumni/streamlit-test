import streamlit as st 
import numpy as np
import pandas as pd 
from PIL import Image

st.title("streamlit 入門")

st.write("data frame")

df = pd.DataFrame(data=[[i for i in range(4)],[i*10 for i in range(4)]])
st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```

```python
import streamlit as st 
import numpy as np
import pandas as pd 

```
"""

oresen_df = pd.DataFrame(data=np.random.rand(20, 3), columns=["a", "b", "c"])
st.line_chart(oresen_df)

area_df = pd.DataFrame(data=[35.69, 139.70] + np.random.rand(100, 2) / [50, 50], columns=["lat", "lon"])
st.map(area_df)

st.write("display image")
image = Image.open("image.png")
st.image(image, caption="numpy", use_column_width=True)

