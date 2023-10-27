package application;
	
import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;



public class Main extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			FXMLLoader loader = new FXMLLoader(getClass().getResource("ExpandedBudget.fxml"));
			loader.setController(this);
			Parent root = loader.load();
			Scene scene = new Scene(root,400,400);
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	@FXML Button btnVisualize;
	@FXML Button btnPlan;
	@FXML Button btnTotal;
	@FXML TextField txtIncome;
	@FXML TextField txtEducation;
	@FXML TextField txtHousing;
	@FXML TextField txtFood;
	@FXML TextField txtTransportation;
	@FXML Label lblResult;
	
    
	public void initialize(){
		
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
