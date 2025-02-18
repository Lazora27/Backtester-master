import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ExtensionProjections': 1.0
        })
    )
