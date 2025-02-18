import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
