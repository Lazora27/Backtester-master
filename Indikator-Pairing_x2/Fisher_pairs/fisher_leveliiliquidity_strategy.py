import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
