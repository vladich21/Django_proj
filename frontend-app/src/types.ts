export interface Container {
    container_id: string;
    type: string;
    status: string;
    location: string | null;
    owner_id: string | null;
    created_at: string;
  }
  export interface User {
    user_id: string,
    name: string,
    email: string,
    role: string,
    created_at: string
  }