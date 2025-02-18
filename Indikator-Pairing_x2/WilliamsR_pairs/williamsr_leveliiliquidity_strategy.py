import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
