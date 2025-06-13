from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AppointmentConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for broadcasting appointment updates related to a specific vehicle.
    
    Each vehicle has a unique group that clients can subscribe to in order to
    receive real-time notifications of appointment changes.
    """
    async def connect(self):
        """
        Called when a WebSocket connection is initiated.

        Retrieves the vehicle ID from the URL route parameters and subscribes
        the socket to a corresponding group for appointment updates.
        """
        self.vehicle_id = self.scope['url_route']['kwargs']['vehicle_id']
        self.group_name = f'appointments_{self.vehicle_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """
        Called when the WebSocket connection is terminated.

        Removes the socket from its associated group.
        """
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_appointment_update(self, event):
        """
        Sends an appointment update message to the connected client.

        This method is invoked by the channel layer using the group name
        and should contain a list of appointments in the event payload.
        """
        appointments = event.get('appointments', [])
        await self.send(text_data=json.dumps({
            "appointments": appointments  
        }))
    
class AppointmentDetailConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for streaming detailed data about a specific appointment.
    
    This includes checklist status, work details, and mileage/fuel updates.
    """
    async def connect(self):
        """
        Called when a WebSocket connection is established.

        Retrieves the appointment ID from the URL and subscribes the socket
        to a group dedicated to that appointment's real-time updates.
        """
        self.appointment_id = self.scope['url_route']['kwargs']['appointment_id']
        self.group_name = f'appointment_details_{self.appointment_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """
        Called when the WebSocket connection is terminated.

        Unsubscribes the socket from the appointment-specific group.
        """
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        """
        Handles messages received from the client.

        Currently unused, but can be implemented to support client-to-server communication.
        """
        pass # Placeholder for potential client-sent commands

    async def send_checklist(self, event):
        """
        Sends checklist information to the client.

        Expected payload format:
            {'checklist': {...}}
        """
        checklist = event['checklist']
        data = {
            'checklist': checklist
        }
        await self.send(text_data=json.dumps(data))

    async def send_works(self, event):
        """
        Sends work-related data to the client.

        Expected payload format:
            {'works': [...]} 
        """
        works = event['works']
        data = {
            'works': works
        }
        await self.send(text_data=json.dumps(data))

    async def send_mileage_and_fuel(self, event):
        """
        Sends mileage and fuel entry data to the client.

        Expected payload format:
            {'mileage': value, 'fuel_entry': value}
        """
        mileage = event['mileage']
        fuel_entry = event['fuel_entry']
        data = {
            'mileage': mileage,
            'fuel_entry': fuel_entry
        }
        await self.send(text_data=json.dumps(data))
