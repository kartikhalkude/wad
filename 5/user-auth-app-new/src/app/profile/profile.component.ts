import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
    selector: 'app-profile',
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './profile.component.html',
    styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
    user: any;

    constructor(private userService: UserService, private router: Router) { }

    ngOnInit() {
        this.user = this.userService.getUser();
        if (!this.user) {
            this.router.navigate(['/login']);
        }
    }

    logout() {
        this.userService.logout();
        this.router.navigate(['/login']);
    }
}