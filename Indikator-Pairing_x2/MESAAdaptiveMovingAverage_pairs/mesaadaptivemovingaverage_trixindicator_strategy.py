import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MESAAdaptiveMovingAverage_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MESAAdaptiveMovingAverage und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'MESAAdaptiveMovingAverage': 1.0,
            'TRIXIndicator': 1.0
        })
    )
