import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private currentUser: any = null;
  private registeredUsers: any[] = [];

  constructor() { }

  login(email: string, password: string): boolean {
    // Find the registered user
    const user = this.registeredUsers.find(u => u.email === email);
    if (user) {
      this.currentUser = {
        name: user.name,
        email: user.email
      };
      return true;
    }
    return false;
  }

  register(user: { name: string, email: string, password: string }): void {
    // Store the registered user
    this.registeredUsers.push(user);
    this.currentUser = {
      name: user.name,
      email: user.email
    };
  }

  getUser() {
    return this.currentUser;
  }

  logout(): void {
    this.currentUser = null;
  }
}
