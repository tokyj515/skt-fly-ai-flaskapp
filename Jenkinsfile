pipeline {

agent any

stages {

stage("build") {

when {

expression {

env.GIT_BRANCH == 'origin/master'

}

}

steps {

echo 'building the applicaiton...'

}

}

stage("test") {

when {

expression {

env.GIT_BRANCH == 'origin/test' || env.GIT_BRANCH == ''

}

}

Jenkins CI Pipeline 생성 실습 5

steps {

echo 'testing the applicaiton...'

}

}

stage("deploy") {

steps {

echo 'deploying the applicaiton...'

}

}

}

}
