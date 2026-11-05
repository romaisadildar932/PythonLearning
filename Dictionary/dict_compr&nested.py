#dict comprehension 
squares = {x: x*x for x in range (1,11)}
print(squares)

#nested dictionary

programming_lang ={
    'python':{
        'name' : 'python',
        'usecase' :['ai','ml','ds']
    },
    'java':{'name':'java',
    'useacse':'app dev'}
}

print(programming_lang)