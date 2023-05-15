FROM postgres:15-bullseye


COPY ./docker/production/postgres/maintenance /usr/production/bin/maintenance

RUN chmod +x /usr/production/bin/maintenance/*

RUN mv /usr/production/bin/maintenance/* /usr/production/bin \
  && rmdir /usr/production/bin/maintenance