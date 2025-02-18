import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
