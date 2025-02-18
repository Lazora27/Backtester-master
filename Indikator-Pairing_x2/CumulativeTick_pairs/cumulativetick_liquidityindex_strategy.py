import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'LiquidityIndex': 1.0
        })
    )
