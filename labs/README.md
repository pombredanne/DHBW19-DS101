# reproducible research sample project

Rproducible research sample project which contains all relevant dependencies.

## executing the analysis

```bash
make image # create reproducible docker image
make notebook # start jupyter notebook server to see results / conduct further analytics

make local-install # install dependencies locally
make local-notebook # locally run the notebook
```

then open a browser and go to: [http://localhost:8888/lab](http://localhost:8888/lab)

it will ask you for a token. The token can be retrieved from the console:

```bash
To access the notebook, open this file in a browser:
    file:///.../Jupyter/runtime/nbserver-52250-open.html
Or copy and paste one of these URLs:
    http://localhost:8888/?token=<<token>>
```

## Requirements

A recent installation of docker.