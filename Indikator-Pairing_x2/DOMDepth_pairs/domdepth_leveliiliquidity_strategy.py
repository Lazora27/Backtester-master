import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
