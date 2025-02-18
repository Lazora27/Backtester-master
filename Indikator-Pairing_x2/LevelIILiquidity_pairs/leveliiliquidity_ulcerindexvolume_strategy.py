import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
