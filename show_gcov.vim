function! ShowGcov()
  highlight GcovColor ctermfg=white ctermbg=red guifg=white guibg=red
  exe 'sign define SignGcov linehl=GcovColor texthl=GcovColor'

  if has('python')
python << EOF
import vim
import re

with open("test/main.cpp.gcov") as f:
    content = f.readlines()
    for line in content:
        matched = re.search(r"^ +#####: +([0-9]+):", line)
        if matched:
            line_num = matched.group(1)
            vim.command('exe \'sign place 9823 line=' + line_num + ' name=SignGcov buffer=\' . winbufnr(0)')
EOF
  else
    echohl Error | echo "ShowGcov() requires vim built with python support" | echohl None
  endif

endfunction
