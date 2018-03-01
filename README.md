## Before Running:
1. Create a bridge network named `celery_test_net`
- `docker network create celery_test_net`
2. Run RabbitMQ as broker
- `docker run -it --rm --network celery_test_net -e RABBITMQ_ERLANG_COOKIE='AnyAlphaNumericStringWillDo' --detach --name messageq_test rabbitmq:3 bash`
- Run server, add user, add vhost and set permissions
    -  `rabbitmq-server -detached`
    -  `rabbitmqctl add_user user1 somepass`
    -  `rabbitmqctl add_vhost hard_word`
    -  `rabbitmqctl set_permissions -p hard_work user1 '.*' '.*' '.*'`

## Run Celery Worker
1. Define a `Dockerfile` to create a container.
2. Build container image
`docker image build . -t celery_server`
3. Run task servers. (Run few tasks server by changing `--name` argument to get better idea)
`docker container run --rm --network celery_test_net --volume $(pwd)/:/home/hardworker/celery-handson/ --name taskserver1 celery_server`

## Test
1.  Running a similer container for testing. Following command will give python shell.
`docker container run --rm -it --network celery_test_net --volume $(pwd)/:/home/hardworker/celery-handson/ --name testmachine celery_server python`

2. Test, obser logs on task servers

``` s
>>> import os
>>> os.chdir('celery-task/src')
>>> from tasks import add
>>> add.delay(4,5)
<AsyncResult: e17b81f7-c608-401e-88d9-10b0aae3d279>
>>> from operations import reverse_string
>>> reverse_string.delay("flsjfkldsfjsdlkfslkfj sklfjslkfjslkfjslkfj skfslk js")
<AsyncResult: d8e3c296-4bf1-4ad7-9589-6061b1e1eee4>
```

## Tear Down
- Stop each container by running `docker container stop <container name>`. This will stop and clean all the container
- Or exit by stopping running process in each container. Stopping main process will stop and clean the container