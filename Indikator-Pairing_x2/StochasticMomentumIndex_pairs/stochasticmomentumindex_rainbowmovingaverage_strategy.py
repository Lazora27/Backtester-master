import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
