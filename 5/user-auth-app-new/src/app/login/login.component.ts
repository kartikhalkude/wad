import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [CommonModule, FormsModule, RouterLink],
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent {
    email: string = '';
    password: string = '';

    constructor(private userService: UserService, private router: Router) { }

    login(): void {
        const success = this.userService.login(this.email, this.password);
        if (success) {
            this.router.navigate(['/profile']);
        } else {
            alert('Invalid Credentials!');
        }
    }
}