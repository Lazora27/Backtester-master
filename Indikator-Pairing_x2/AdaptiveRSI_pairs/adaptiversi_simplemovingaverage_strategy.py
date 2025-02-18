import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
