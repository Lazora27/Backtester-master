import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
