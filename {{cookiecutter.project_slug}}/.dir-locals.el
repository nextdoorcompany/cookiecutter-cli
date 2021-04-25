;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil . ((eval . (progn
                   (setq-local compile-command
                               (expand-file-name "env/{{cookiecutter.scripts_or_bin}}/doit" default-directory))))))
 (python-mode . ((mode . black-on-save)
                 (eval . (progn
                           (setq-local black-command
                                       (expand-file-name "env/{{cookiecutter.scripts_or_bin}}/black" default-directory))
                           (setq-local python-shell-virtualenv-root
                                       (expand-file-name "env" default-directory)))))))
