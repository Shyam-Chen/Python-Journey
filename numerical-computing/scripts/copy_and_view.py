
__generated_with = "0.23.0"

# %%
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# %%
copied = arr.copy()
viewed = arr.view()

# %%
arr[0] = 9

print(f"arr    = {arr}")
print(f"copied = {copied}")
print(f"viewed = {viewed}")