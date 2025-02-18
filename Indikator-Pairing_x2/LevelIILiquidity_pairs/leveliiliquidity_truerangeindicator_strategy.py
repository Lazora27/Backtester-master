import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
