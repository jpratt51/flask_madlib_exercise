const word_form = document.getElementsByClassName('text_input')
for (let i = 0; i < word_form.length; i++) {
    word_form[i].setAttribute("maxlength", "15")
    word_form[i].setAttribute("minlength", "3")
}

