'''Write a function called linear_search_product the takes the list of products and a target product names as input .The function should perform a linear search to find the target product in the list and return a list of indices of all accurances of the product is not found'''
def linearSearchProduct(productList
,targetProduct):
    indices=[]
    for index,product in enumerate(productList):
        if product==targetProduct:
            indices.append(index)
    return indices
#Example usage
products=["pen","pencil","eraser","pen","note","pen"]
target="pen"
target2="paper"
result=linearSearchProduct(products,target)
print(result)