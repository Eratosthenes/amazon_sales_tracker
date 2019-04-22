from config import API
import bottlenose
import pdb

amazon = bottlenose.Amazon(API['ID'], API['API key'], API['Name'])
response = amazon.ItemLookup(ItemId="B007OZNUCE")
pdb.set_trace()
