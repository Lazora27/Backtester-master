import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'BuyingPressure': 1.0
        })
    )
