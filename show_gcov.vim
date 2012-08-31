function! ShowGcov()
  echo "running ShowGcov()"

  if !exists("b:ShowGcov_sign_number")
    let b:ShowGcov_sign_number = 1
  endif

  let current_line = line(".")

  exe 'sign define SignGcov linehl=SignColor texthl=SignColor'
  exe 'sign place ' . b:ShowGcov_sign_number . ' line=' . current_line . ' name=SignGcov buffer=' . winbufnr(0)

  let b:ShowGcov_sign_number = b:ShowGcov_sign_number + 1

endfunction
