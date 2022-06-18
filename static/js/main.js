function showProjects(array){
	const project_template = document.querySelector('#project-template')
	const project = project_template.content.querySelector('.project')
	const projects_container = document.querySelector('.projects-container')

	for(let i = 0; i < array.length; i++){
		let project_block = project.cloneNode(true)

        project_block.querySelector('.image').src = array[i].img
		project_block.querySelector('.name_project').href = array[i].url
		project_block.querySelector('.name_project').innerText = array[i].name
        project_block.querySelector('.info-btn-url').href = array[i].url
		projects_container.append(project_block)
	}
}

function showQuetions(array){
	const questions_template = document.querySelector('#quetions-template')
	const question = questions_template.content.querySelector('.question-answer')
	const about_container = document.querySelector('.about-container')

	for(let i = 0; i < array.length; i++){
		let question_block = question.cloneNode(true)

        question_block.querySelector('.question-btn').innerText = array[i].question
		question_block.querySelector('.answer-text').innerText = array[i].answer
		about_container.append(question_block)
	}
}

function redirect(url) {
    return location = `${url}`
}

const year = document.getElementById('year')
year.innerText = (new Date()).getFullYear()

const login_btn = document.querySelector('.login-btn')
login_btn.addEventListener('click', () => {
    redirect('/profile')
})

const discord_btn = document.querySelector('.discord-btn')
discord_btn.addEventListener('click', () => {
	redirect('https://discord.com/invite/r2jmqs6AaM')
})