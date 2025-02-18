import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MovingAverage': 1.0
        })
    )
