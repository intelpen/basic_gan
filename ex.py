# [(3, +),  (5,  +),  (5, +),  (4 *)  (5 *) (6 *)  (7 +)] #the + is added as sentinel

p = 1
s = 0
exp_list = [(3, '+'),  (5,  '+'),  (5, '+'),  (4, '*') , (5, '*'), (6, '*'),  (7,'+')]
for el in exp_list: 
    if el[1] == '+':
        s = s + p*el[0]
        p=1
    elif el[1] == '*':
        p = p * el[0]

print(s)
print(p)

# UPDATE wp_options SET option_value = 'http://34.28.72.19.nip.io/' WHERE option_name = 'siteurl' OR option_name = 'home';


# wp search-replace 'http://airl.ro' 'http://34.28.72.19.nip.io' --allow-root

