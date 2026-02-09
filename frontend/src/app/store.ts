import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import documentsReducer from '../features/documents/documentsSlice';
import qaReducer from '../features/qa/qaSlice';

export const store = configureStore({
    reducer: {
        auth: authReducer,
        documents: documentsReducer,
        qa: qaReducer,
    }
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;