
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()



pytrend.build_payload(kw_list=['Coronavirus'])
related_queries = pytrend.related_queries()
print(list((((related_queries)["Coronavirus"])["top"])["query"].to_frame()["query"]))



