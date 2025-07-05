<script setup lang="ts">
import InputError from '@/components/InputError.vue';
import TextLink from '@/components/TextLink.vue';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import AuthBase from '@/layouts/AuthLayout.vue';
import { Head, useForm } from '@inertiajs/vue3';
import { LoaderCircle } from 'lucide-vue-next';

const props = defineProps<{
    status?: string;
    canResetPassword: boolean;
    providers: Array<any>
}>();

const form = useForm({
    email: '',
    password: '',
    remember: false,
});

const submit = () => {
    form.post('/login', {
        onFinish: () => form.reset('password'),
    });
};
</script>

<template>
    <AuthBase title="Log in to your account" description="Enter your email and password below to log in">
        <Head title="Log in" />

        <form @submit.prevent="submit" class="flex flex-col gap-6">
            <div class="grid gap-6">
                <div class="grid gap-2">
                    <Label for="email">Email address</Label>
                    <Input
                        id="email"
                        type="email"
                        required
                        autofocus
                        :tabindex="1"
                        autocomplete="email"
                        v-model="form.email"
                        placeholder="email@example.com"
                    />
                    <InputError :message="form.errors.email" />
                </div>

                <div class="grid gap-2">
                    <div class="flex items-center justify-between">
                        <Label for="password">Password</Label>
                        <TextLink v-if="canResetPassword" href="#" class="text-sm" :tabindex="5">
                            Forgot password?
                        </TextLink>
                    </div>
                    <Input
                        id="password"
                        type="password"
                        required
                        :tabindex="2"
                        autocomplete="current-password"
                        v-model="form.password"
                        placeholder="Password"
                    />
                    <InputError :message="form.errors.password" />
                    <div class="text-left text-sm text-muted-foreground">
                        <TextLink href="/forgot-password" :tabindex="5">Forgot yout password?</TextLink>
                    </div>

                </div>

                <div class="flex items-center justify-between">
                    <Label for="remember" class="flex items-center space-x-3">
                        <Checkbox id="remember" v-model="form.remember" :tabindex="3" />
                        <span>Remember me</span>
                    </Label>
                </div>

                <Button type="submit" class="mt-4 w-full" :tabindex="4" :disabled="form.processing">
                    <LoaderCircle v-if="form.processing" class="h-4 w-4 animate-spin" />
                    Log in
                </Button>
            </div>

            <div class="text-center text-sm text-muted-foreground">
                ou login com:
                    <a 
                    class="text-foreground pl-2 underline decoration-neutral-300 underline-offset-4 transition-colors duration-300 ease-out hover:decoration-current! dark:decoration-neutral-500"
                    v-for="provider in props.providers" 
                    :href="`/login/${provider.toLowerCase()}`" 
                    :tabindex="5">
                    
                    <Button as="a" class="mr-3">
                        <svg widths="30px" height="200px" width="200px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 455.73 455.73" xml:space="preserve" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path style="fill:#DD4B39;" d="M0,0v455.73h455.73V0H0z M265.67,247.037c-7.793,51.194-45.961,80.543-95.376,80.543 c-55.531,0-100.552-45.021-100.552-100.552c0-55.517,45.021-100.538,100.552-100.538c26.862,0,50.399,9.586,67.531,26.226 l-28.857,28.857c-9.773-9.846-23.147-15.094-38.674-15.094c-32.688,0-59.189,27.874-59.189,60.548 c0,32.703,26.501,59.768,59.189,59.768c27.397,0,48.144-13.243,54.129-39.758h-54.129v-40.38h95.131 c1.142,6.506,1.72,13.315,1.72,20.37C267.144,234.025,266.638,240.69,265.67,247.037z M386.419,234.517h-35.233v35.218H326.16 v-35.218h-35.233v-25.041h35.233v-35.233h25.026v35.233h35.233V234.517z"></path> </g></svg>
                        {{ provider }}
                    </Button>
                    </a>
            </div>
            <div class="text-center text-sm text-muted-foreground">
                Don't have an account?
                <TextLink href="/register" :tabindex="5">Sign up</TextLink>
            </div>
        </form>
    </AuthBase>
</template>