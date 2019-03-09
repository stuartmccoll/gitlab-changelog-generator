workflow "Main Workflow" {
    on = "push"
    resolves = "Unit Tests"
}

action "Unit Tests" {
    uses = "./actions/test"
}
