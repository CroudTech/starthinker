###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

from starthinker.util.project import from_parameters
from starthinker.util.storage import bucket_create, bucket_access


@from_parameters
def bucket(project, task):
  if project.verbose:
    print('BUCKET', task['bucket'])

  # create bucket
  bucket_create(task['auth'], project.id, task['bucket'])
  bucket_access(
      task['auth'],
      project.id,
      task['bucket'],
      emails=task.get('emails', []),
      groups=task.get('groups', []))


if __name__ == '__main__':
  bucket()
