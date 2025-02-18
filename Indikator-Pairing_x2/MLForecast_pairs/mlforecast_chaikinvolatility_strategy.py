import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
