import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
