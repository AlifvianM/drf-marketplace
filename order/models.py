from django.db import models

# Create your models here.

class Payment(models.Model):
    """Model definition for Payment."""

    # TODO: Define fields here
    name    = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Payment."""

        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        """Unicode representation of Payment."""
        return self.name


class Order(models.Model):
    """Model definition for Order."""

    # TODO: Define fields here
    # product     = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    address     = models.TextField(blank=True)
    phone       = models.CharField(max_length=50, blank=True)
    # payment     = models.ForeignKey(Payment, on_delete=models.CASCADE) 
    created_at  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return "ORDER ID : {}, {}".format(self.pk, self.created_at)


class OrderItem(models.Model):
    """Model definition for OrderItem."""

    # TODO: Define fields here
    order   = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    price   = models.FloatField()
    quantity= models.IntegerField(default=1)

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return "Order item ID {}, product {}".format(self.pk, self.product)
