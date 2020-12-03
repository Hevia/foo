use azure_functions::{
    bindings::{HttpRequest, HttpResponse},
    func,
};

#[func]
pub fn turkey(req: HttpRequest) -> HttpResponse {
    const ingrident_modifiers: [f32; 11] = [
        0.05, 0.66, 0.13, 0.2, 0.4, 0.13, 0.13, 0.13, 0.06, 2.4, 15.0,
    ];
    let ingrident_names = [
        "Salt",
        "Water",
        "Brown Sugar",
        "Shallots",
        "Cloves of garlic",
        "Whole peppercorns",
        "Dried Juniper berries",
        "Fresh rosemary",
        "Thyme",
        "Brine time",
        "Roast time",
    ];
    let turkey_weight = req.body();
    eprintln!("{}", turkey_weight);
    return "Hello from Rust!".into();
}
