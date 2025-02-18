import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
