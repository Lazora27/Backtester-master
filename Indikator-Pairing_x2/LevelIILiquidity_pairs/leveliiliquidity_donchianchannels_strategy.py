import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'DonchianChannels': 1.0
        })
    )
