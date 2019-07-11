'''
pip upgrade all wheels
'''

import subprocess

# get the list of wheels
com_list_o = 'pip list -o' 
p = subprocess.Popen(com_list_o, shell=True, stdout=subprocess.PIPE)
out = p.communicate()[0]
# utf-8
out = str(out, 'utf-8')

need_update = []
for i in out.splitlines()[2:]:
    need_update.append(i.split(' ')[0])

# upgrade
for nu in need_update:
    com_update = 'pip install -U {py}'.format(py=nu)
    print("start:", com_update)
    subprocess.call(com_update)
    print("----------{com} done -----------\n".format(com=com_update))


print("check update:")
subprocess.call(com_list_o)
