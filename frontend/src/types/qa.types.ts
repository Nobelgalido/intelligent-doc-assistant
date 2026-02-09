export interface Source {
    document_id: string;
    document_title: string;
    chunk_id: string;
    page_number: number;
    text_preview: string;
    similarity_score: number;
}

export interface Question {
    id: string;
    question_text: string;
    answer_text: string;
    sources: Source[];
    confidence_score: number;
    processing_time_ms: number;
    created_at: string;
    is_helpful?: boolean;
}

export interface Conversation {
    id: string;
    title: string;
    questions_count: number;
    latest_question?: Question;
    created_at: string;
    updated_at: string;
}

export interface AskQuestionData {
    question: string;
    document_ids?: string[];
    conversation_id?: string;
}