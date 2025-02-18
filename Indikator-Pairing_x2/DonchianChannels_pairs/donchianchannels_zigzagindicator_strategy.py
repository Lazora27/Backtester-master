import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
