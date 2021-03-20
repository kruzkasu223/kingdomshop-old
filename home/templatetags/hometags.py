from django import template
from django.urls import reverse
from order.models import Cart
from home.models import Policy, CompanySocialMedia

register = template.Library()

@register.simple_tag(takes_context=True)
def active_on(context, name):
    try: 
        if context['request'].resolver_match.url_name == name:
            return 'active'
    except:
        return ''
    return ''
    


urls_name = [
    'account_login',
    'account_signup',
    'account_logout',
    'account_change_password',
    'account_set_password',
    'account_inactive',
    'account_email',
    'account_email_verification_sent',
    'account_confirm_email',
    'account_reset_password',
    'account_reset_password_done',
    'account_reset_password_from_key',
    'account_reset_password_from_key_done'
]

@register.simple_tag(takes_context=True)
def accounts_page(context):
    for names in urls_name:
        try:
            if context['request'].resolver_match.url_name == names:
                return 'hidden_footer'
        except:
            return ''
    return ''
    


@register.simple_tag
def cart_count(userid):
    count = Cart.objects.filter(user_id=userid).count()
    return count
    


@register.simple_tag
def policy_list():
    return Policy.objects.all()
    

@register.simple_tag
def sm_list():
    return CompanySocialMedia.objects.all()
    

@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url