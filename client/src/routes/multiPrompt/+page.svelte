<script lang="ts">
	import Swal from 'sweetalert2';
	import { api, getErrorMessage } from '$api';
  
	let prompt1 = '';
	let prompt2 = '';
	let responseText = '';
  
	async function handleSubmit() {
	  Swal.fire({
		title: 'Procesando...',
		text: 'Por favor espera mientras se procesan tus prompts.',
		icon: 'info',
		allowOutsideClick: false,
		showConfirmButton: false,
		willOpen: () => {
		  Swal.showLoading();
		}
	  });
  
	  try {
		const response = await api.post('/multiPrompt', { prompt1, prompt2 });
		if (response.status === 200) {
		  const responses = response.data;
		  responseText = responses.map(res => `Pregunta: ${res.question}\nRespuesta: ${res.response}`).join('\n\n');
		  Swal.fire({
			title: 'Prompts recibidos',
			text: 'Los prompts fueron enviados y recibidos correctamente.',
			icon: 'success',
			timer: 3000,
			showConfirmButton: false
		  });
		}
	  } catch (error) {
		console.error('Error al enviar los prompts:', error);
		Swal.fire({
		  title: 'Error',
		  text: 'Hubo un problema al enviar los prompts',
		  icon: 'error',
		  timer: 3000,
		  showConfirmButton: false
		});
	  }
	}
  </script>
  
  <main class="container mx-auto p-4">
	<h1 class="text-2xl font-bold mb-4">Multi Prompt</h1>
	
	<form on:submit|preventDefault={handleSubmit} class="space-y-4 flex">
	  <div class="flex-1 mr-4">
		<div>
		  <label for="prompt1" class="block text-sm font-medium text-gray-700">Prompt 1</label>
		  <textarea id="prompt1" bind:value={prompt1} rows="4" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Escribe tu prompt aquí..."></textarea>
		</div>
		
		<div class="mt-4">
		  <label for="prompt2" class="block text-sm font-medium text-gray-700">Prompt 2</label>
		  <textarea id="prompt2" bind:value={prompt2} rows="15" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm resize-y overflow-auto" placeholder="Escribe tu prompt aquí..."></textarea>
		</div>
		
		<div class="mt-4">
		  <button type="submit" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
			Enviar
		  </button>
		</div>
	  </div>
  
	  <div class="flex-1 ml-4">
		<div>
		  <label for="response" class="block text-sm font-medium text-gray-700">Response</label>
		  <textarea id="response" bind:value={responseText} rows="20" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm resize-y overflow-auto" placeholder="La respuesta aparecerá aquí..." readonly></textarea>
		</div>
	  </div>
	</form>
  </main>
  
  <style>
	.container {
	  max-width: 1200px;
	}
  </style>