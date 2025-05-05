import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-register',
    standalone: true,
    imports: [CommonModule, FormsModule, RouterLink],
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.css']
})
export class RegisterComponent {
    name: string = '';
    email: string = '';
    password: string = '';

    constructor(private userService: UserService, private router: Router) { }

    register(): void {
        this.userService.register({
            name: this.name,
            email: this.email,
            password: this.password
        });
        alert('Registered Successfully!');
        this.router.navigate(['/login']);
    }
} 