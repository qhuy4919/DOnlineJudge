import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import loginAPI from '../api/loginAPI';
import registerAPI from '../api/registerAPI';
import logoutAPI from '../api/logoutAPI';
export const loginUser = createAsyncThunk(
    '/login',
    async ({username, password }, thunkAPI) => {
        try {
            const response = await loginAPI.login({username, password});
            if(response.token !== null){
                localStorage.setItem('token', response.token);
                localStorage.setItem('role', response.user.admin_type);
                localStorage.setItem('username', response.user.username);
                localStorage.setItem('userId', response.user.id);
                localStorage.setItem('userInformation', JSON.stringify(response.user));
                return response;
            }else{
                alert("fail to fetch tokem Login")
            }
        } catch (error) {
            console.log('Fail to login: ', error);
            thunkAPI.rejectWithValue(error.response.json());
        }
    }
);

export const registerUser = createAsyncThunk(
    '/register',
    async (data, thunkAPI) => {
        try {
            // console.log(data);
           await registerAPI.register(data);
        } catch (error) {
            console.log('Fail to register: ', error);
            thunkAPI.rejectWithValue(error.response.json());
        }
    }
)
export const logoutUser = createAsyncThunk(
    '/logout',
    async (thunkAPI) => {
        try {
            await logoutAPI.logout();

        } catch (error) {
            console.log('Fail to logout: ', error);
            thunkAPI.rejectWithValue(error.response.json());
        }
    }
)
export const userSlice = createSlice({
    name: 'user',
    initialState: {
        username: '',
        email: '',
        isLoginSuccess: false,
        isLoginError: false,
        isRegisterSuccess: false,
        isRegisterError: false,
        isFeching: false,
        errorMessage: '',
    },
    reducers:{
        clearState: (state) => {
            state.isLoginSuccess = false;
            state.isLoginError = false;
            state.isRegisterSuccess = false;
            state.isRegisterError = false;      
            return state;
        },
        userClear: (state) =>{
            state.userInformation = {};
        }
    },

    extraReducers:{
        //login feching status
        [loginUser.fulfilled]: (state, {payload}) =>{
            state.username = payload.user.username;
            state.isFeching = false;
            state.isLoginSuccess = true;
            return state;
        },
        [loginUser.pending]: (state) =>{
            state.isFeching = true;
        },
        [loginUser.rejected]: (state, {payload}) => {
            state.isLoginError = true;
            state.isFeching = false;
            state.errorMessage = 'Username or password is wrong';
        },
        //register fetching status
        [registerUser.fulfilled]: (state , {payload}) => {
            state.isFeching = false;
            state.isRegisterSuccess = true;
        },
        [registerUser.rejected]: (state, { payload }) => {
            state.isFeching = false;
            state.isRegisterError = true;
            state.errorMessage = 'Register fail';
        },
        [registerUser.pending]: (state) => {
            state.isFeching = true;
        },
        //logout
        [logoutUser.fulfilled]: (state) => {
            state.isFeching = false;
            state.isSuccess = true;
        },
        [logoutUser.rejected]: (state) => {
            state.isFeching = false;
            state.isError = true;
        },
        [logoutUser.pending]: (state) => {
            state.isFeching = true;
        },



    },
})
export const { clearState, userClear } = userSlice.actions;

export const userSelector = (state) => state.user;