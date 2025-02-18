import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
