import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BarStrength
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BarStrength': 1.0
        })
    )
