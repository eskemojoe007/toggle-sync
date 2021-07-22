from toggl.TogglPy import Toggl
import keyring

toggl = Toggl()
toggl.setAPIKey(keyring.get_password("toggl", "primary"))

response = toggl.request("https://api.track.toggl.com/api/v8/workspaces")
print(response)
for workspace in response:
    print("workspace name: %s  workspace id: %s" % (workspace['name'], workspace['id']))


# Our workspace is 4615636
response = toggl.request("https://api.track.toggl.com/reports/api/v2/weekly", parameters={'user_agent':'david.folkner@gmail.com', 'workspace_id': 4615636})
print(response)