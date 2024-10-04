import json

val_file,test_file,report_file=input(),input(),input()

def check_values(vals,value_dict):
    for test in vals:   
        if 'values' in test:
            check_values(test['values'],value_dict)
        if 'value' in test:
            test['value']=value_dict[test['id']]
 


with open(val_file, "r") as v:
    value_data=json.load(v)
    value_list=[e for e in value_data['values']]
value_dict={a['id']: a['value'] for a in value_list}# словарь значений теста     
with open(test_file) as t:
    test_data=json.load(t) 
    test_list=[e for e in test_data['tests']] 
check_values(test_list,value_dict)    

print(test_list)
test_result={"tests":test_list}
       
with open(report_file,"w") as r:
    json.dump(test_result,r, indent=2)