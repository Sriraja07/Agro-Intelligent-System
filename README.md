# Agro-Intelligent-System
<p>Agro-Intelligent System is a Machine Learning based Web application.It is used for farming strategy to increase the production without affecting from any 
climatic changes.System predicting based on weather and soil parameters.</p>
<p>Agro-Intelligent System Consists of three main parts,they are
<ul>
<li>Crop Recommender</li>
<li>Fertilizer Advisor</li>
<li>Crop Yield Predictor</li>
</ul></p>
<h2>Crop Recommender</h2>
<p>&emsp;Crop Recommender is used to recommend the sowing crop based on weather and soil parameters. Consider the soil factor like Nitrogen, Phosphorous, Potassium, 
soil pH value and Weather parameters like Rainfall, temperature, moisture and humidity. We use open weather API to get the current value of Rainfall, moisture, 
humidity by getting parameters from user location.After applying the different machine learning algorithms for the dataset, the machine learning algorithm Random 
forest classifier show the best accuracy score almost 99.986%. we trained model by using Random forest classifier algorithm for crop recommending model. This model 
will be saved, and the farmers can easily get the sowing crop recommending by giving their farmer soil type characteristics, top soil and pH as the input to the
system,etc.</p>
<h2>Fertilizer Advisor</h2>
<p>&emsp;Fertilizer Advisor is used to advice how to use fertilizer based on crop and soil parameters.Consider Consider the soil factor like Nitrogen, Phosphorous, 
Potassium, soil pH value and crop. Based on the soil value it will say the fertilizer and how to use it.So farmer's or any person who want to cultivate ,can easily 
get information about the fertilizer.</p>
<h2>Crop Yield Predictor</h2>
<p>&emsp;Yield Predictor is used to Predict the crop yield .Consider the soil factor like Nitrogen, Phosphorous, Potassium, soil pH value and Weather parameters 
like Rainfall, temperature, moisture and humidity. We use open weather API to get the current value of Rainfall, moisture, humidity by getting parameters from user
location. After applying the different machine learning algorithms for the dataset, we trained models of the crop recommending model. Based on Mean Absolute error, 
Random Forest machine learning algorithm shows the low MAE value. Crop yield which will use the Random Forest Regression machine learning algorithm to trained the 
model and test the model. Which will outcomes the best accuracy score as 97.7654325897.So the farmers can easily get the crop yield prediction by giving their 
farmer's soil type characteristics, top soil and pH as the input to the system,etc.</p>
