import React from 'react';
import { Container, Typography, Button, Box, Paper } from '@mui/material';
import { useAppDispatch, useAppSelector } from '../app/hooks';
import { logout } from '../features/auth/authSlice';
import { useNavigate } from 'react-router-dom';

const Dashboard: React.FC = () => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const { user } = useAppSelector((state) => state.auth);

  const handleLogout = () => {
    dispatch(logout());
    navigate('/login');
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h3" gutterBottom>
          Welcome to Intelligent Doc Assistant! 🎉
        </Typography>
        <Typography variant="h5" color="text.secondary" gutterBottom>
          Hello, {user?.first_name} {user?.last_name}!
        </Typography>
        <Box sx={{ mt: 4 }}>
          <Typography variant="body1" paragraph>
            Email: {user?.email}
          </Typography>
          <Typography variant="body1" paragraph>
            Username: {user?.username}
          </Typography>
          <Typography variant="body1" paragraph>
            Total Documents: {user?.total_documents}
          </Typography>
          <Typography variant="body1" paragraph>
            Total Questions: {user?.total_questions}
          </Typography>
        </Box>
        <Button variant="contained" color="error" onClick={handleLogout} sx={{ mt: 2 }}>
          Logout
        </Button>
      </Paper>
    </Container>
  );
};

export default Dashboard;
