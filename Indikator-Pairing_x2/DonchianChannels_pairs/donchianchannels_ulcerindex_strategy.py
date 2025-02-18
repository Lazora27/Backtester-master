import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'UlcerIndex': 1.0
        })
    )
