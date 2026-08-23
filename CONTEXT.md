# Tracker

The Tracker provides a shared view of work across customers. It organizes work as Customer to Project to Task so each concept has one consistent meaning across tracker workflows.

## Language

**Customer**:
A person or organization for whom work is being done. A Customer contains Projects.
_Avoid_: Client, account, company

**Project**:
A distinct direction or stream of work under a Customer. A Project groups Tasks but does not itself represent an actionable unit of work.
_Avoid_: Workstream, initiative, engagement

**Task**:
The operational unit of work under a Project. Progress and responsibility are tracked at the Task level.
_Avoid_: Item, ticket, to-do, activity

**Task Candidate**:
Potential work discovered from communication or discussion that has not yet been accepted as a Task. A Task Candidate becomes a Task only after the user confirms both the work and its Project.
_Avoid_: Untriaged task, draft task

**Triage**:
The review in which Task Candidates are accepted, assigned to a Project, or ignored. Acceptance creates a Task; discovery alone does not.
_Avoid_: Sweep, filing