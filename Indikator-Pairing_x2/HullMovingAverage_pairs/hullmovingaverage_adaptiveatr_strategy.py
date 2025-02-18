import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'AdaptiveATR': 1.0
        })
    )
