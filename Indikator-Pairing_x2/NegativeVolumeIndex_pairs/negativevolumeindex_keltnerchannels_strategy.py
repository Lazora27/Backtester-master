import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
