FROM ubuntu:latest

WORKDIR /app
ADD . /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip nginx && \
    pip3 install requests && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    python3 ./src/my_pkg/main.py

# Check if nginx user exists, and if not, create it
RUN if ! id -u nginx &>/dev/null; then useradd -r -s /usr/sbin/nologin nginx; fi

# Set permissions
RUN chown -R nginx:nginx /var/www/html && chmod -R 755 /var/www/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# FROM ubuntu:latest
# 
# WORKDIR /app
# ADD . /app
# 
# RUN apt-get update
# RUN apt-get install -y python3 python3-pip nginx && \
#     pip3 install requests && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* && \
#     python3 ./src/my_pkg/main.py
# RUN id -u nginx &>/dev/null || useradd -r -s /usr/sbin/nologin nginx && \
#     chown -R nginx:nginx /var/www/html && chmod -R 755 /var/www/html
# 
# EXPOSE 80
# 
# CMD ["nginx", "-g", "daemon off;"]