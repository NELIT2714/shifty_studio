loadProjects()
loadQuestions()

function loadProjects(){
    let xhr = new XMLHttpRequest()
    xhr.open('GET', '/api/get/projects')
    xhr.responseType = 'json'
    xhr.send()
    xhr.addEventListener('load', () => {
        window.projects = xhr.response
        showProjects(window.projects)
    })
}

function loadQuestions(){
    let xhr = new XMLHttpRequest()
    xhr.open('GET', '/api/get/questions')
    xhr.responseType = 'json'
    xhr.send()
    xhr.addEventListener('load', () => {
        window.quetions = xhr.response
        showQuetions(window.quetions)

        const elements = [...document.querySelectorAll('.question-btn')];
        elements.forEach(accordion);
    })
}
