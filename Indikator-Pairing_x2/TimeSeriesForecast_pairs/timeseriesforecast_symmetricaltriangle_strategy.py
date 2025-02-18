import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
