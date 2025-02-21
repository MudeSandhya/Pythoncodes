import json
D={'name':'venky','batch':'m17','timing':'4.00','attendance':89}
with open('detail.json','w') as fobj:
    content=json.dumps(D)
    fobj.write(content)
    
