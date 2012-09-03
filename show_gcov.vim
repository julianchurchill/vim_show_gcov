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
cmd_folder = "$HOME/.vim/plugin"
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
import show_gcov

buf = vim.eval('bufname("%")')
filename = vim.eval('fnamemodify("'+buf+'",":p")')
gcov_file = show_gcov.find_gcov_file( filename );
if gcov_file == "":
    gcov_file = "test/main.cpp.gcov"

if gcov_file == "":
    vim.command('echohl Error | echo "ShowGcov() gcov file for \'' + filename + '\' not found" | echohl None')
else:
    f = open(gcov_file)
    line_num = 1
    for line in f:
        matched = re.search(r"^ +#####", line)
        if matched:
            line_number = str(line_num)
            matched = re.search(r"^ +#####: +([0-9]+):", line)
            if matched:
                line_number = matched.group(1)
            vim.command('exe \'sign place \' . b:ShowGcov_sign_number . \' line=' + line_number + ' name=SignGcov buffer=\' . winbufnr(0)')
            vim.command('let b:ShowGcov_sign_number = b:ShowGcov_sign_number + 1')
        line_num = line_num + 1
    f.close()
EOF
  else
    echohl Error | echo "ShowGcov() requires vim built with python support" | echohl None
  endif

endfunction
