import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
