document.addEventListener('DOMContentLoaded', () => {
    const downloadBtns = document.querySelectorAll('.mainBlock_filesBlock_fileBlock_buttonDownload')
    
    downloadBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            PNotify.success({
                title: 'Success',
                text: 'Download started',
                delay: 2000
            })
        })
    })

    const deleteForms = document.querySelectorAll('form[action*="delete"]')
    
    deleteForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const isConfirmed = confirm('Are you sure you want to delete this file?')
            
            if (!isConfirmed) {
                e.preventDefault()
            } else {
                PNotify.info({
                    title: 'Deleting',
                    text: 'File is being deleted...',
                    delay: 2000
                })
            }
        })
    })
})