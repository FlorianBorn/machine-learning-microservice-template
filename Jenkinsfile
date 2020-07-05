node {
    checkout(scm)
    config = readProperties(file: ".env")
    echo "${config}"
    runtime_image = "${config.repository}/${config.runtime_image_name}:${config.runtime_image_tag}"
    branch_name = "master"

    System.setProperty("org.jenkinsci.plugins.durabletask.BourneShellScript.LAUNCH_DIAGNOSTICS", "true") // for debugging

    stage('Run Unit Tests') {
        img = docker.image("${runtime_image}")
        img.inside {
            sh "pytest tests/data/ tests/model/"
        }
    }




}