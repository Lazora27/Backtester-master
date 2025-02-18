import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
