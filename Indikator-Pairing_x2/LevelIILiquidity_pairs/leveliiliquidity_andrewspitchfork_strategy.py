import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
