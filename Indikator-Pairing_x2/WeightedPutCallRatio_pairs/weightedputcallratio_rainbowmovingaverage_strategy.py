import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
