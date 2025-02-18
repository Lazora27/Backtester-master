import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
