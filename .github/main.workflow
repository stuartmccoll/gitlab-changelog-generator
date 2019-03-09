workflow "Main Workflow" {
    on = "pull_request"
    resolves = "Unit Tests"
}

action "Unit Tests" {
    uses = "./actions/test"
}
