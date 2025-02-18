import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AverageLogRange': 1.0
        })
    )
