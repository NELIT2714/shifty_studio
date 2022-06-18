const password2 = document.getElementById('password2')
const password = document.getElementById('password')
const message_error_span = document.querySelector('.message-error')
const create_account_btn = document.getElementById('create-account-btn')

password.addEventListener('change', () => {
	if(password.value != password2.value || password2.value != password.value) {
		message_error_span.textContent = 'Пароли не совпадают'
		create_account_btn.classList.add('disabled')
		create_account_btn.classList.remove('login-in-account')
		create_account_btn.disabled = true
	} else {
		message_error_span.textContent = null
		create_account_btn.classList.remove('disabled')
		create_account_btn.classList.add('login-in-account')
		create_account_btn.disabled = false
	}
})

password2.addEventListener('change', () => {
	if(password.value != password2.value || password2.value != password.value) {
		message_error_span.textContent = 'Пароли не совпадают'
		create_account_btn.classList.add('disabled')
		create_account_btn.classList.remove('login-in-account')
		create_account_btn.disabled = true
	} else {
		message_error_span.textContent = null
		create_account_btn.classList.remove('disabled')
		create_account_btn.classList.add('login-in-account')
		create_account_btn.disabled = false
	}
})