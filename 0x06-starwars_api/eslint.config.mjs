import globals from 'globals';
import pluginJs from '@eslint/js';
import { FlatCompat } from '@eslint/eslintrc';
import { fixupConfigRules } from '@eslint/compat';

const compat = new FlatCompat();
/** @type {import('eslint').Linter.Config[]} */
export default [
  ...fixupConfigRules(
    compat.config({
      extends: ['semistandard']
    })
  ),
  { files: ['**/*.js'], languageOptions: { sourceType: 'commonjs' } },
  { languageOptions: { globals: globals.browser } },
  pluginJs.configs.recommended
];
