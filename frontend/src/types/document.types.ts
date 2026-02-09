export interface Document {
    id: string;
    title: string;
    file: string;
    file_type: 'pdf' | 'docx' | 'txt' | 'md';
    file_size: number;
    status: 'pending' | 'processing' | 'completed' | 'failed';
    processing_error?: string;
    page_count: number;
    word_count: number;
    chunks_count: number;
    created_at: string;
    updated_at: string;
    processed_at?: string;
}

export interface DocumentUploadData {
    title: string;
    file: File;
    file_type: 'pdf' | 'docx' | 'txt' | 'md';
    collection?: string;
}