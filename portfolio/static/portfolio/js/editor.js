document.addEventListener('DOMContentLoaded', () => {
    
    const form = document.getElementById('editorForm')
    const createBtn = document.getElementById('createCvBtn')
    
    const previewEmail = document.querySelector('.js-preview-email')
    const previewPhone = document.querySelector('.js-preview-phone')
    const previewGithub = document.querySelector('.js-preview-github')
    const previewSummary = document.querySelector('.js-preview-summary')
    const previewWork = document.querySelector('.js-preview-work')
    const previewEducation = document.querySelector('.js-preview-education')
    const previewSkillsContainer = document.querySelector('.js-preview-skills-container')

    const inputMapping = {
        'work_email': previewEmail,
        'phone_number': previewPhone,
        'summary': previewSummary,
        'work_experience': previewWork,
        'education': previewEducation
    }

    const checkFormValidity = () => {
        let isValid = true
        const inputs = form.querySelectorAll('input, textarea')

        inputs.forEach(input => {
            if (input.type === 'hidden' || input.type === 'checkbox') return
            if (input.name.toLowerCase().includes('github')) return
            
            if (!input.value.trim()) {
                isValid = false
            }
        })

        if (isValid) {
            createBtn.disabled = false
            createBtn.style.opacity = '1'
            createBtn.style.cursor = 'pointer'
        } else {
            createBtn.disabled = true
            createBtn.style.opacity = '0.5'
            createBtn.style.cursor = 'not-allowed'
        }
    }

    const handleTextInput = (e) => {
        const input = e.target
        const name = input.name
        
        if (inputMapping[name]) {
            inputMapping[name].textContent = input.value
        }

        if (name.toLowerCase().includes('github')) {
            updateGithubPreview(input.value)
        }

        checkFormValidity()
    }

    const updateGithubPreview = (url) => {
        if (!url) {
            previewGithub.textContent = ''
            previewGithub.removeAttribute('href')
            return
        }

        let nickname = url.replace(/\/$/, '').split('/').pop()
        
        previewGithub.textContent = nickname
        const finalUrl = url.startsWith('http') ? url : `https://github.com/${nickname}`
        previewGithub.href = finalUrl
    }

    const handleSkillChange = () => {
        const checkedSkills = form.querySelectorAll('input[name="skills"]:checked')
        
        previewSkillsContainer.innerHTML = ''

        checkedSkills.forEach(checkbox => {
            const label = checkbox.parentElement.querySelector('label')
            const skillName = label ? label.textContent.trim() : checkbox.value

            const skillDiv = document.createElement('div')
            skillDiv.className = 'centerBlock_resumeBlock_textBlock_skillsBlock_skillsItemsBlock_skillItem'
            skillDiv.textContent = skillName
            
            previewSkillsContainer.appendChild(skillDiv)
        })
        
        checkFormValidity()
    }

    const inputs = form.querySelectorAll('input, textarea')
    
    inputs.forEach(input => {
        if (input.type === 'checkbox') {
            input.addEventListener('change', handleSkillChange)
        } else {
            input.addEventListener('input', handleTextInput)
        }
    })

    createBtn.addEventListener('click', (e) => {
        e.preventDefault()
        
        if (createBtn.disabled) return

        let isValid = true
        
        inputs.forEach(input => {
             const name = input.name
             if (input.type === 'hidden' || input.type === 'checkbox') return
             if (name.toLowerCase().includes('github')) return

             if (!input.value.trim()) {
                 isValid = false
                 if (typeof PNotify !== 'undefined') {
                    PNotify.error({
                        title: 'Error',
                        text: `Field "${name}" is required!`,
                        delay: 3000
                    })
                 }
             }
        })

        if (isValid) {
            form.submit()
        }
    })

    checkFormValidity()
})