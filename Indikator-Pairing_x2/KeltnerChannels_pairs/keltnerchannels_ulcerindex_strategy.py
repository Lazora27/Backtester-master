import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'UlcerIndex': 1.0
        })
    )
