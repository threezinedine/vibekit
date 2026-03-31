# Guide to organize the architecture of the frontend project

## Tree Structure

```bash
frontend/
├── src/
│   ├── stories/ # storybook setup
│   ├── components/
│       ├── button/
│           ├── Button.tsx
│           ├── Button.scss
│           ├── Button.test.tsx     # must have for components/
│           ├── Button.stories.tsx  # must have for components/
│           └── index.tsx
│       ├── form/
│       └── toast/
│           ├── Toast.tsx
│           ├── Toast.scss
│           ├── Toast.test.tsx
│           ├── Toast.stories.tsx
│           ├── stores/
│               └── toastStore.ts
│           └── index.tsx
│   ├── layout/
│       ├── default/
│           ├── DefaultLayout.tsx
│           ├── DefaultLayout.scss
│           └── index.tsx
│   ├── pages/
│       ├── login/
│           ├── LoginPage.tsx
│           ├── LoginPage.scss
│           └── index.tsx
│   ├── features/
│       ├── auth/
│           ├── components/
│               ├── AuthForm/
│                   ├── AuthForm.tsx
│                   ├── AuthForm.scss
│                   ├── AuthForm.test.tsx    # optional for components in features/
│                   ├── AuthForm.stories.tsx # optional for components in features/
│                   └── index.tsx
│           ├── services/
│           ├── hooks/
│           └── utils/
│   ├── services/
│   ├── hooks/
│   ├── utils/
│   └── App.tsx
├── public/
├── package.json
└── README.md
```
