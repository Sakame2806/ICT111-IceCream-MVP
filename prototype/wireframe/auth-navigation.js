(function () {
    function getCurrentUser() {
        try {
            return JSON.parse(sessionStorage.getItem('icecream_user'));
        } catch {
            return null;
        }
    }

    const style = document.createElement('style');
    style.textContent = `
        .account-dropdown {
            position: fixed;
            z-index: 5000;
            width: 190px;
            padding: 8px;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            background: #fff;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.16);
        }
        .account-dropdown[hidden] { display: none; }
        .account-dropdown-name {
            padding: 8px 10px 10px;
            overflow: hidden;
            color: #6b7280;
            font-size: 12px;
            text-overflow: ellipsis;
            white-space: nowrap;
            border-bottom: 1px solid #f0f0f0;
        }
        .account-dropdown button {
            display: block;
            width: 100%;
            margin: 0;
            padding: 10px;
            border: 0;
            border-radius: 7px;
            color: #374151;
            background: transparent;
            font: inherit;
            font-size: 14px;
            text-align: left;
            cursor: pointer;
        }
        .account-dropdown button:hover,
        .account-dropdown button:focus {
            background: #f3f4f6;
            outline: none;
        }
        .account-dropdown .logout-button { color: #dc2626; }
        .account-dropdown .logout-button:hover,
        .account-dropdown .logout-button:focus { background: #fef2f2; }
    `;
    document.head.appendChild(style);

    const dropdown = document.createElement('div');
    dropdown.className = 'account-dropdown';
    dropdown.setAttribute('role', 'menu');
    dropdown.hidden = true;
    document.body.appendChild(dropdown);
    let activeAvatar = null;

    function closeDropdown() {
        dropdown.hidden = true;
        if (activeAvatar) {
            activeAvatar.setAttribute('aria-expanded', 'false');
        }
        activeAvatar = null;
    }

    function createMenuButton(label, className, action) {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = className;
        button.setAttribute('role', 'menuitem');
        button.textContent = label;
        button.addEventListener('click', action);
        return button;
    }

    function openDropdown(avatar) {
        if (activeAvatar === avatar && !dropdown.hidden) {
            closeDropdown();
            return;
        }
        if (activeAvatar) {
            activeAvatar.setAttribute('aria-expanded', 'false');
        }

        const user = getCurrentUser();
        dropdown.innerHTML = '';
        if (user?.user_id) {
            const name = document.createElement('div');
            name.className = 'account-dropdown-name';
            name.textContent = `${user.nickname} (${user.user_id})`;
            dropdown.append(
                name,
                createMenuButton('个人主页', 'profile-button', () => {
                    window.location.href = 'User-Profile.html';
                }),
                createMenuButton('Logout', 'logout-button', () => {
                    sessionStorage.removeItem('icecream_user');
                    window.location.href = 'login.html';
                })
            );
        } else {
            dropdown.appendChild(
                createMenuButton('Login', 'login-button', () => {
                    window.location.href = 'login.html';
                })
            );
        }

        dropdown.hidden = false;
        activeAvatar = avatar;
        avatar.setAttribute('aria-expanded', 'true');
        const rect = avatar.getBoundingClientRect();
        const dropdownWidth = 190;
        const left = Math.max(
            8,
            Math.min(window.innerWidth - dropdownWidth - 8, rect.right - dropdownWidth)
        );
        dropdown.style.left = `${left}px`;
        dropdown.style.top = `${rect.bottom + 8}px`;
        dropdown.querySelector('button')?.focus();
    }

    document.querySelectorAll(
        'header .icon-group > .avatar, .navbar .nav-right > .avatar'
    ).forEach(avatar => {
        avatar.style.cursor = 'pointer';
        avatar.setAttribute('role', 'button');
        avatar.setAttribute('tabindex', '0');
        avatar.setAttribute('aria-label', 'Open account menu');
        avatar.setAttribute('aria-haspopup', 'menu');
        avatar.setAttribute('aria-expanded', 'false');
        avatar.addEventListener('click', event => {
            event.stopPropagation();
            openDropdown(avatar);
        });
        avatar.addEventListener('keydown', event => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                event.stopPropagation();
                openDropdown(avatar);
            }
        });
    });

    dropdown.addEventListener('click', event => event.stopPropagation());
    document.addEventListener('click', closeDropdown);
    document.addEventListener('keydown', event => {
        if (event.key === 'Escape') {
            const avatar = activeAvatar;
            closeDropdown();
            avatar?.focus();
        }
    });
    window.addEventListener('resize', closeDropdown);
    window.addEventListener('scroll', closeDropdown, true);
})();
