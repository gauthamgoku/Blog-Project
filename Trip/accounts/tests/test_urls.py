from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import base, articles, newest_articles, oldest_articles, delete_article, edit_article, comments, newest_comment ,oldest_comment, comment_approve, comment_remove, custom_article, about, contact, register_admin, register_author, register_user, login_user, logout_view, mumbai_view, goa_view, delhi_view, hyderabad_view



class TestUrls(SimpleTestCase):

    def test_base_url_is_resolved(self):
        url = reverse('base')
        print(resolve(url))
        self.assertEquals(resolve(url).func, base)

    def test_articles_url_is_resolved(self):
        url = reverse('articles')
        print(resolve(url))
        self.assertEquals(resolve(url).func, articles)

    def test_newest_articles_url_is_resolved(self):
        url = reverse('newest_articles')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newest_articles)

    def test_oldest_articles_url_is_resolved(self):
        url = reverse('oldest_articles')
        print(resolve(url))
        self.assertEquals(resolve(url).func, oldest_articles)

    def test_delete_articles_url_is_resolved(self):
        url = reverse('delete_articles', kwargs={'id':1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_article)

    def test_edit_articles_url_is_resolved(self):
        url = reverse('edit_articles', kwargs={'id':1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_article)

    def test_comments_url_is_resolved(self):
        url = reverse('comments')
        print(resolve(url))
        self.assertEquals(resolve(url).func, comments)

    def test_newest_comment_url_is_resolved(self):
        url = reverse('newes_commentt', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, newest_comment)

    def test_oldest_comment_url_is_resolved(self):
        url = reverse('oldest_comment', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, oldest_comment)

    def test_comment_approve_url_is_resolved(self):
        url = reverse('comment_approve', kwargs={'id':1,'tittle':'some-slugs'})
        print(resolve(url))
        self.assertEquals(resolve(url).func, comment_approve)

    def test_comment_remove_url_is_resolved(self):
        url = reverse('comment_remove', kwargs={'id':1,'tittle':'some-slugs'})
        print(resolve(url))
        self.assertEquals(resolve(url).func, comment_remove)

    def test_custom_article_url_is_resolved(self):
        url = reverse('custom_article')
        print(resolve(url))
        self.assertEquals(resolve(url).func, custom_article)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)

    def test_register_admin_url_is_resolved(self):
        url = reverse('register_admin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_admin)

    def test_register_user_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_user)

    def test_register_author_url_is_resolved(self):
        url = reverse('register_author')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_author)

    def test_login_user_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_view_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)

    def test_mumbai_view_url_is_resolved(self):
        url = reverse('mumbai')
        print(resolve(url))
        self.assertEquals(resolve(url).func, mumbai_view)

    def test_goa_view_url_is_resolved(self):
        url = reverse('goa')
        print(resolve(url))
        self.assertEquals(resolve(url).func, goa_view)

    def test_delhi_view_url_is_resolved(self):
        url = reverse('delhi')
        print(resolve(url))
        self.assertEquals(resolve(url).func, delhi_view)

    def test_hyderabad_view_url_is_resolved(self):
        url = reverse('hyderbabad')
        print(resolve(url))
        self.assertEquals(resolve(url).func, hyderabad_view)
