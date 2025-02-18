import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'DonchianChannels': 1.0
        })
    )
