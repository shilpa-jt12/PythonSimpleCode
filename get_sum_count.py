#get the count of 'sum' in main string input
txt = "sumsummitsumaassumet"

txt = list(txt)
final_lst = [i for i in txt if i not in 'aeiouAEIOU']
print(''.join(final_lst))
