import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und OpenInterest
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'OpenInterest': 1.0
        })
    )
