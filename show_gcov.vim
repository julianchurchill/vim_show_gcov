function! ShowGcov_remove_signs()
  let sign_id = 9823
  while sign_id < b:ShowGcov_sign_number
    exe 'sign unplace ' . sign_id
    let sign_id = sign_id + 1
  endwhile
  let b:ShowGcov_sign_number = 9823
endfunction

function! ShowGcov()
  highlight GcovColor ctermfg=white ctermbg=red guifg=white guibg=red
  exe 'sign define SignGcov linehl=GcovColor texthl=GcovColor'

  if !exists("b:ShowGcov_sign_number")
    let b:ShowGcov_sign_number = 9823
  endif

  if has('python')
python << EOF
import vim
import re
import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
import show_gcov

gcov_file = show_gcov.find_gcov_file( "" );
if gcov_file == "":
    gcov_file = "test/main.cpp.gcov"

with open(gcov_file) as f:
    content = f.readlines()
    for line in content:
        matched = re.search(r"^ +#####: +([0-9]+):", line)
        if matched:
            line_num = matched.group(1)
            #vim.command('exe \'sign place 9823 line=' + line_num + ' name=SignGcov buffer=\' . winbufnr(0)')
            vim.command('exe \'sign place \' . b:ShowGcov_sign_number . \' line=' + line_num + ' name=SignGcov buffer=\' . winbufnr(0)')
            vim.command('let b:ShowGcov_sign_number = b:ShowGcov_sign_number + 1')
EOF
  else
    echohl Error | echo "ShowGcov() requires vim built with python support" | echohl None
  endif

endfunction
