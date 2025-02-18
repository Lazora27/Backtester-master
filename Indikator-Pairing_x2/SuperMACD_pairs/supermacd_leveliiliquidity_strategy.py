import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
