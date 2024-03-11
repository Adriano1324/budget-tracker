FROM node:20-slim
COPY . /app
WORKDIR /app
RUN npm install -g pnpm

RUN pnpm install
RUN pnpm build
RUN npx playwright install --with-deps
