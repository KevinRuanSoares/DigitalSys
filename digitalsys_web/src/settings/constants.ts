export const ENVIRONMENT = {
  development: {
    url: 'http://localhost:8181/api/v1/',
  },
} as const;

export const API_URL = ENVIRONMENT.development.url;
