import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'KeltnerChannels': 1.0
        })
    )
