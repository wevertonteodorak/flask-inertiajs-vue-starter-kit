from src._core.utils.common import env


auth_config = {

    'Google': {
        'client_id': env('GOOGLE_CLIENT_ID'),
        'client_secret': env('GOOGLE_CLIENT_SECRET'),
        'meta_url': env('GOOGLE_META_URL'),
    },

    'Microsoft': {
        'client_id': env('MICROSOFT_CLIENT_ID'),
        'client_secret': env('MICROSOFT_CLIENT_SECRET'),
        'meta_url': env('MICROSOFT_META_URL'),
    }
}