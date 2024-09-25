from typing import List

"""
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
"""


class Solution:
    def findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str],
    ) -> List[str]:
        ans = []
        allIngredients = set([s for i in ingredients for s in i])
        for s in supplies:
            if s not in allIngredients:
                supplies.remove(s)

        for s in supplies:
            for i in ingredients:
                if s in i:
                    i.remove(s)

        q = []
        for p, i in enumerate(ingredients):
            if len(i) == 0:
                ans.append(recipes[p])
                if recipes[p] in allIngredients:
                    q.append(recipes[p])

        while len(q) > 0:
            ns = q.pop()
            for p, i in enumerate(ingredients):
                if ns in i:
                    i.remove(ns)
                    if len(i) == 0:
                        ans.append(recipes[p])
                        if recipes[p] in allIngredients:
                            q.append(recipes[p])
        return ans


print(
    Solution().findAllRecipes(
        recipes=["bread", "sandwich", "burger"],
        ingredients=[
            ["yeast", "flour"],
            ["bread", "meat"],
            ["sandwich", "meat", "bread"],
        ],
        supplies=["yeast", "flour", "meat"],
    )
)
