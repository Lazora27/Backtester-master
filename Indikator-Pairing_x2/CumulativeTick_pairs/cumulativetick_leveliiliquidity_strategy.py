import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
