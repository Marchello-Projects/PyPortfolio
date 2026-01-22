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

  const submitBtn = document.getElementById('submitBtn')
  const usernameInput = document.getElementById('id_username')
  const passwordInput = document.getElementById('id_password')

  const allInputs = [usernameInput, passwordInput]

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
})