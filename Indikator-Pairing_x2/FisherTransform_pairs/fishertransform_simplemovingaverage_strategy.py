import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
