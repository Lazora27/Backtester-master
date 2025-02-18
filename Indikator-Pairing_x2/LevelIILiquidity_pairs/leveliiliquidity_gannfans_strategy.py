import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und GannFans
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'GannFans': 1.0
        })
    )
