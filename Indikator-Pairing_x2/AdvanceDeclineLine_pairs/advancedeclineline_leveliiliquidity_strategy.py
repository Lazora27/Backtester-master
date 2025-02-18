import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
