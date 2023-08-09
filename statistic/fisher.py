from scipy.stats import fisher_exact
import pandas as pd
data = pd.DataFrame({"Понравился":[4,0],"Не понравился":[0,4]}).transpose()
data.columns = ["Лекарство №1", "Лекарство №2"]
data = data.transpose()
res, p = fisher_exact(data)
print(p)