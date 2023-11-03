def Query(dict, query):
        for i in query:
            if i in dict:
                return dict.get(i)
            else:
                return None


dict = {1: "abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
print(Query(dict, query))
