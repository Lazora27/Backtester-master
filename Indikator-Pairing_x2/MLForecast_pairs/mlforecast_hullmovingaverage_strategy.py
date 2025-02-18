import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HullMovingAverage': 1.0
        })
    )
