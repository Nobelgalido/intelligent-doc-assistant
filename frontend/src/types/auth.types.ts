export interface User {
    id: string;
    email: string;
    username: string;
    first_name: string;
    last_name: string;
    avatar?: string;
    total_documents: number;
    total_questions: number;
}

export interface LoginCredentials {
    email: string;
    password: string;

}

export interface RegisterData {
    email: string;
    username: string;
    password: string;
    password_confirm: string;
    first_name: string;
    last_name: string;
}

export interface AuthResponse {
    access: string;
    refresh: string;
    user: User;
}

export interface AuthState {
    user: User | null;
    accessToken: string | null;
    refreshToken: string | null;
    isAuthenticated: boolean;
    loading: boolean;
    error: string | null;
}