import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'LiquidityIndex': 1.0
        })
    )
