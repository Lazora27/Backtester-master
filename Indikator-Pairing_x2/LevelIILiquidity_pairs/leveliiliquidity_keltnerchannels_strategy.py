import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'KeltnerChannels': 1.0
        })
    )
