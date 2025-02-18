import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
