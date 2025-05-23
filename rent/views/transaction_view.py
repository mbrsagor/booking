from django.db import transaction
from django.contrib import messages
from django.views import generic, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect

from profit.models import Project, Transaction, Customer, Profit, Worker


# Create transaction by project ID
@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class CreateTransactionByProject(View):
    success_message = "Transaction created successfully."
    template_name = "transaction/create_transaction.html"

    def get(self, request, pk):
        project_id = get_object_or_404(Project, pk=pk)
        # Project ID set session variable
        request.session["project_id"] = project_id.id
        projects = Project.objects.all()
        labors = Worker.objects.filter(worker_type=1)
        vendors = Worker.objects.filter(worker_type=2)
        context = {"projects": projects, "labors": labors, "vendors": vendors, 'project_id': project_id.id}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Get data from request
        project_id = request.session.get('project_id')
        source_type = request.POST.get("source_type")
        amount = request.POST.getlist("amount[]")
        notes = request.POST.getlist("notes[]")
        quantity = request.POST.getlist("quantity[]")
        date = request.POST.getlist("date[]")
        worker_ids = request.POST.getlist("worker[]")

        # Combine the data into a list of dictionaries for each Profit
        _data = [
            {
                "date": date,
                "quantity": quantity,
                "amount": amount,
                "worker_ids": worker_ids,
                "notes": notes,
            }
            for date, quantity, amount, worker_ids, notes in zip(
                date, quantity, amount, worker_ids, notes
            )
        ]

        # Create a new Transaction
        transaction = Transaction(project_id=project_id, source_type=source_type)
        transaction.save()

        # Create Profit instances and associate them with the Transaction
        for profit_data in _data:
            worker_id = int(profit_data["worker_ids"])
            #  Retrieve the specific Worker instance
            worker_instance = Worker.objects.get(id=worker_id)

            # Create the Profit instance, associating it with the Labor instance
            profit = Profit(
                amount=profit_data["amount"],
                quantity=profit_data["quantity"],
                date=profit_data["date"],
                notes=profit_data["notes"],
                worker=worker_instance,
            )
            profit.save()

            # Associate the Profit instance with the Transaction
            transaction.profits.add(profit)
        # Save the transaction after adding all profits
        transaction.save()
        # Destroy project_id session
        request.session.pop('project_id', None)  # Safe delete without KeyError
        messages.success(request, "Transaction created successfully!")
        return redirect(request.path)


@method_decorator(login_required(login_url="/user/login"), name="dispatch")
class TransactionListView(generic.ListView):
    model = Transaction
    context_object_name = "transactions"
    template_name = "transaction/transaction_listview.html"


@method_decorator(login_required(login_url="/user/login"), name="dispatch")
class TransactionDetailsView(generic.DetailView):
    model = Transaction
    context_object_name = "transaction"
    template_name = "transaction/transaction_detail.html"

    def get_context_data(self, **kwargs):
        # Get the profits associated with the transaction and add them to the context
        expense = []
        context = super().get_context_data(**kwargs)
        context["profits"] = context["transaction"].profits.all()
        transaction = context["transaction"].profits.all()
        for tran in transaction:
            expense.append(tran.total_amount)
        # Calculate and add the total expense to the context
        round_amount = rounded_value = round(sum(expense), 2)
        context["total_expense"] = round_amount
        return context


@method_decorator(login_required(login_url="/user/login"), name="dispatch")
class TransactionUpdateView(View):
    template_name = "transaction/update_transaction.html"

    def get(self, request, pk):
        transaction = Transaction.objects.get(id=pk)
        projects = Project.objects.all()
        labors = Worker.objects.filter(worker_type=1)
        vendors = Worker.objects.filter(worker_type=2)
        context = {"projects": projects, "labors": labors, "vendors": vendors, "transaction": transaction}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        # Retrieve and validate form data
        project_id = request.POST.get("project")
        source_type = request.POST.get("source_type")
        amounts = request.POST.getlist("amount[]")
        notes_list = request.POST.getlist("notes[]")
        quantities = request.POST.getlist("quantity[]")
        dates = request.POST.getlist("date[]")
        worker_ids = request.POST.getlist("worker[]")

        # Combine data for profits
        profits_data = [
            {
                "date": date,
                "quantity": quantity,
                "amount": amount,
                "worker_id": worker_id,
                "notes": notes
            }
            for date, quantity, amount, worker_id, notes in zip(
                dates, quantities, amounts, worker_ids, notes_list
            )
        ]

        # Update transaction and associated profits
        try:
            # Retrieve or create the transaction
            transaction = get_object_or_404(Transaction, pk=pk)
            transaction.project_id = project_id
            transaction.source_type = source_type
            transaction.save()

            # Clear old profits associated with the transaction
            transaction.profits.all().delete()

            # Create and bulk insert new profits
            profits = []
            for profit_data in profits_data:
                worker = get_object_or_404(Worker, pk=int(profit_data["worker_id"]))
                profit = Profit(
                    amount=profit_data["amount"],
                    quantity=profit_data["quantity"],
                    date=profit_data["date"],
                    notes=profit_data["notes"],
                    worker=worker,
                )
                profits.append(profit)
            Profit.objects.bulk_create(profits)
            # Re-associate profits with the transaction
            transaction.profits.set(profits)
            messages.success(request, "Transaction updated successfully!")
            return redirect("transaction_update", pk=pk)
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect("transaction_update", pk=pk)


# Transaction update V2
@method_decorator(login_required(login_url="/user/login"), name="dispatch")
class ProfitUpdateNewView(SuccessMessageMixin, generic.UpdateView):
    model = Profit
    form_class = ProfitModelForm
    success_message = "Profit updated successfully."
    template_name = "transaction/update_transaction.html"

    def form_valid(self, form):
        # Get POST data
        source_type = self.request.POST.get("source_type")
        worker_id = self.request.POST.get("worker")

        # Validate the source type and worker ID
        if source_type and worker_id:
            try:
                # Ensure source_type is an integer
                source_type = int(source_type)
                # Query for Worker with specific worker_type
                worker = Worker.objects.get(id=worker_id, worker_type=source_type)
                form.instance.worker = worker  # Assign the worker to the form
            except Worker.DoesNotExist:
                form.add_error(None, "Invalid worker for the selected source type.")
                return self.form_invalid(form)
            except Exception as e:
                form.add_error(None, "An unexpected error occurred.")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Source type and worker must be selected.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("transaction_update", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labors"] = Worker.objects.filter(worker_type=1, status=True)
        context["vendors"] = Worker.objects.filter(worker_type=2, status=True)
        return context

