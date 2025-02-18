import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
