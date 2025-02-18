import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
