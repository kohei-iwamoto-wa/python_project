FROM mysql:8
# RUN touch /var/log/mysql/mysqld.log

# ADD /data/my.cnf /etc/mysql/conf.d/my.cnf
# RUN chmod 644 /etc/mysql/my.cnf
RUN rm -rf /var/lib/mysql/*
# RUN mkdir /var/lib/mysql
RUN chown root:root /var/lib/mysql/
