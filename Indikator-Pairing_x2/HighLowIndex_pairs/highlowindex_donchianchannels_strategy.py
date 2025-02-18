import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
