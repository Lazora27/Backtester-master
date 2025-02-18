import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'BuyingPressure': 1.0
        })
    )
