const url = 'https://edtech-dj.herokuapp.com/api/textbook-list/';

fetch(url).then((resp) => resp.json())
			.then(function(data){
				console.log('Data:', data)
      })