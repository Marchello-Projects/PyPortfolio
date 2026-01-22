document.addEventListener('DOMContentLoaded', function () {
  const serverErrorsScript = document.getElementById('server-errors')
  if (serverErrorsScript) {
    try {
      const errors = JSON.parse(serverErrorsScript.textContent)
      for (const [field, messages] of Object.entries(errors)) {
        messages.forEach(error => {
          if (typeof PNotify !== 'undefined') {
            PNotify.error({
              text: error.message,
              delay: 4000,
              addClass: 'translucent'
            })
          }
        })
      }
    } catch (e) {
      console.error(e)
    }
  }

  const form = document.getElementById('registerForm')
  const submitBtn = document.getElementById('submitBtn')

  const usernameInput = document.getElementById('id_username')
  const emailInput = document.getElementById('id_email')
  const pass1Input = document.getElementById('id_password1')
  const pass2Input = document.getElementById('id_password2')

  const allInputs = [usernameInput, emailInput, pass1Input, pass2Input]

  function checkFieldsFilled() {
    let allFilled = true

    allInputs.forEach(input => {
      if (!input || !input.value.trim()) {
        allFilled = false
      }
    })

    if (allFilled) {
      submitBtn.disabled = false
      submitBtn.style.opacity = '1'
      submitBtn.style.cursor = 'pointer'
    } else {
      submitBtn.disabled = true
      submitBtn.style.opacity = '0.5'
      submitBtn.style.cursor = 'not-allowed'
    }
  }

  allInputs.forEach(input => {
    if (input) {
      input.addEventListener('input', checkFieldsFilled)
    }
  })

  form.addEventListener('submit', function (event) {
    let hasError = false
    const passValue = pass1Input.value
    const passConfirmValue = pass2Input.value

    if (passValue.length < 8) {
      if (typeof PNotify !== 'undefined') {
        PNotify.error({
          title: 'Weak password',
          text: 'The password must contain at least 8 characters.',
          delay: 3000,
          addClass: 'translucent'
        })
      }
      hasError = true
    }

    if (/^\d+$/.test(passValue)) {
      if (typeof PNotify !== 'undefined') {
        PNotify.error({
          title: 'Weak password',
          text: 'The password cannot consist entirely of numbers.',
          delay: 3000,
          addClass: 'translucent'
        })
      }
      hasError = true
    }

    if (passValue !== passConfirmValue) {
      if (typeof PNotify !== 'undefined') {
        PNotify.error({
          title: 'Error',
          text: 'The passwords do not match.',
          delay: 3000,
          addClass: 'translucent'
        })
      }
      hasError = true
    }

    if (hasError) {
      event.preventDefault()
    }
  })
})