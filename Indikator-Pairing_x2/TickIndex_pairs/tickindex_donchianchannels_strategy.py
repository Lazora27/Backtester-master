import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
