import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'LiquidityIndex': 1.0
        })
    )
