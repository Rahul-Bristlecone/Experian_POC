def function(n):
    if n > 4000:
        return
    print(n)
    function(n * 2)
    print(n)


function(1000)
