# __2025_06_29_chihlee_postgres__

#### 上課的連結

https://meet.google.com/qbi-juyg-amj

致理_postgres_星期日


docker run -d --name my-conda hsinchung/miniforge_uv_npx:1.3 tail -f /dev/null

docker run -d --name my-conda roberthsu2003/conda_uv_npx tail -f /dev/null


#window,使用intel或amd cpu
docker run --platform linux/amd64 -it --name python-postgres -d roberthsu2003/conda_uv_npx

docker run --platform linux/amd64 -it --name python-postgres -d hsinchung/miniforge_uv_npx:1.3

docker run -d --name my-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=raspberry -e POSTGRES_DB=postgres -p 5432:5432 postgres:latest

