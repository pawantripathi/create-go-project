#!/usr/bin/python

import sys
import os
import json
import textwrap


class ProjectGenerator:
    """ Simple class for generating a preset folder heirarchy"""

    def __init__(self, projectname):
        """__init__ [Initializer for ProjectGenerator with a projectName]

        Args:
            projectname ([string]): [Name for the project/root directory]
        """
        self.projectname = projectname

    def create(self):
        """create [Entry method that will generate the folder heirarchy]
        """
        self.createdirectorystructure()
        self.writeconfigtemplate()
        self.writeservicetemplate()
        self.writemaindotgo()

    def createdirectorystructure(self):
        """createdirectorystructure generates required folders
        """
        dirs = [f'./{self.projectname}',
                f'./{self.projectname}/src/{self.projectname}',
                f'./{self.projectname}/config',
                f'./{self.projectname}/etc/systemd/system',
                f'./{self.projectname}/docs', ]

        for dir in dirs:
            if not os.path.exists(dir):
                os.makedirs(dir)

    def writemaindotgo(self):
        """writemaindotgo creates a simple main.go inside src/projectName
        """
        body = '''
        package main
        import "fmt"

        func main(){
            fmt.Println("Generated via create-go-project")
        }
        '''
        with open(f'./{self.projectname}/src/{self.projectname}/main.go', 'w') as outfile:
            outfile.write(textwrap.dedent(body))

    def writeconfigtemplate(self):
        """writeconfigtemplate writes a sample config.json under config folder
        """
        data = {
            "svc": f'{self.projectname}',
            "ht": "localhost",
            "log_file": "/path/to/logfile.log",
            "log_file_max_size": 50000000,
        }
        with open(f'./{self.projectname}/config/config.json', 'w') as outfile:
            json.dump(data, outfile)

    def writeservicetemplate(self):
        """writeservicetemplate writes a template .service file under etc/systemd/system
        """
        with open(f'./{self.projectname}/etc/systemd/system/{projectname}.service', 'w') as outfile:
            lines = [
                '[Unit]\n',
                f'Description={self.projectname}\n',
                '\n',
                '[Service]\n',
                'User=root\n',
                'Group=root\n',
                f'WorkingDirectory=/usr/local/{self.projectname}\n',
                f'ExecStart=/usr/local/{self.projectname}/{self.projectname}_linux-amd64 /usr/local/{self.projectname}/config.json\n',
                '\n',
                '[Install]\n',
                'WantedBy=multi-user.target\n'

            ]
            outfile.writelines(lines)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Command usage: python3 {__file__} <projectName>')
    else:
        arglist = sys.argv
        scriptname = arglist[0]
        projectname = arglist[1]

        ProjectGenerator(projectname).create()
