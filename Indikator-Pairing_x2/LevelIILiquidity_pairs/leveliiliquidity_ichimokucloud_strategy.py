import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'IchimokuCloud': 1.0
        })
    )
