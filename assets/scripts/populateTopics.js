const populateTopics = () => {
    const isOverflow = ({clientHeight, scrollHeight}) => {
        return scrollHeight > clientHeight;
    };

    const makeTopicTag = (topicName) => {
        const topic = document.createElement('ul');
        topic.classList.add('topic');
        topic.innerText = topicName;
        topic.addEventListener('click', filterByTopic);
        return topic;
    };

    const makeButton = () => {
        const showBtn = document.createElement('button');
        showBtn.innerText = 'Show more';
        showBtn.classList.add('hidden');
        showBtn.addEventListener('click', () => {
            topicList.classList.toggle('topic-truncate');
            showBtn.innerText == 'Show more' ? 
            showBtn.innerText = 'Show less' : 
            showBtn.innerText = 'Show more';
        });
        return showBtn;
    }

    const topicContainer = document.querySelector('#topic-list--container');
    const topicList = document.querySelector('#topic-list');
    const topics = [
        ...new Set(
            [...document.querySelectorAll('.topic')]
                .map(i => i.innerText)
        )
    ].sort();

    topics.forEach(topicName => {
        topicList.appendChild(makeTopicTag(topicName));
    });

    const showBtn = makeButton();
    topicContainer.appendChild(showBtn);

    window.addEventListener('resize', function() {
        if (isOverflow(topicList) || topicList.clientHeight > window.innerHeight * .2) {
            showBtn.classList.remove('hidden');
        } else showBtn.classList.add('hidden')
    }, true)

    if (isOverflow(topicList)) {
        showBtn.classList.remove('hidden');
    } 
};

function filterByTopic() {
    const selected = document.querySelector('#topic-list>.topic.selected');
    if (selected) selected.classList.remove('selected');

    const selection = this.innerText;
    const articles = document.querySelectorAll('.project');

    if (!selected || selected.innerText !== selection) {
        this.classList.add('selected');

        articles.forEach(project => {
            project.classList.add('hidden');

            const topics = [...project.children[2].children];
            for (let topic of topics) {
                if (topic.innerText.trim() === selection.trim()) {
                    project.classList.remove('hidden');
                }
            }
        });
    } else {
        this.classList.remove('selected');

        articles.forEach(project => project.classList.remove('hidden'));
    }

};

document.addEventListener('DOMContentLoaded', populateTopics);