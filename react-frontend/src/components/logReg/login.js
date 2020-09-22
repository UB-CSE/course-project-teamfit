import React from "react";
import loginImg from "../../logo.svg";

const formValid = ({ formErrors, ...rest }) => {
  let valid = true;

  // validate form errors being empty
  Object.values(formErrors).forEach(val => {
    val.length > 0 && (valid = false);
  });

  // validate the form was filled out
  Object.values(rest).forEach(val => {
    val === null && (valid = false);
  });

    return valid;
};

const emailRegex = RegExp(
  /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
);

export default class Login extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            uEmail: null,
            uPassword: null,
            formErrors: {
                uEmail: "",
                uPassword: "",
            }
        }
    }

    handleSubmit = e => {
        e.preventDefault();
        if (formValid(this.state)){
            console.log(`
            --SUBMITTING-- 
            E-MAIL: ${this.state.uEmail}
            PASSWORD: ${this.state.uPassword}
            `)
        }
        else{
            console.error("FORM INVALID")
        }
    }
    handleChange = e => {
        e.preventDefault();
        const {name,value} = e.target;
        let formErrors = this.state.formErrors;
        console.log(name)
        switch (name) {
            case 'uEmail':
                formErrors.uEmail = emailRegex.test(value) ? "":'Please enter E-mail address';
                break;
            case 'uPassword':
                formErrors.uPassword = value.length < 1 ? 'Please enter password':"";
                break;
            default:
            break;
        }
        this.setState({formErrors, [name]:value}, ()=> console.log(this.state))
    };

    render(){
        const{formErrors} =this.state;
        return <div className="wrapper">
                <div className="header">*Temp* TeamFit Homepage Link/Logo *Temp*</div>
                    <div className="form-wrapper">
                        <div className="image">
                            <img src={loginImg} width="200" height="200" alt="Login Image" />
                        </div>
                        <h1>Sign in to Account</h1>
                        <form onSubmit={this.handleSubmit} noValidate>
                            <div className="allForms">
                                <div className="uEmail">
                                    <label htmlFor="uEmail">E-mail</label>
                                    <input className={formErrors.uEmail.length > 0 ? "error" : null} type="email" name="uEmail" placeholder="example@gmail.com" onChange={this.handleChange}/>
                                    {formErrors.uEmail.length > 0 && ( <span className="errorMessage">{formErrors.uEmail}</span> )}
                                </div>
                                <div className="uPassword">
                                    <label htmlFor="uPassword">Password</label>
                                    <input className={formErrors.uPassword.length > 0 ? "error" : null} type="password" name="uPassword" placeholder="password"onChange={this.handleChange}/>
                                    {formErrors.uPassword.length > 0 && ( <span className="errorMessage">{formErrors.uPassword}</span> )}
                                </div>
                                <div className="loginBtn">
                                    <button type="submit">Sign-in</button>
                                </div>
                            </div>
                        </form>
                    </div>
            <div className="footer">
                <small>Don't have an account?</small>
                <small><p><a href="/register">Register here!</a></p></small>
            </div>
        </div>
    }
}
