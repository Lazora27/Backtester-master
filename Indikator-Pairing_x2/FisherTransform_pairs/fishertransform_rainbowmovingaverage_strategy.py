import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
