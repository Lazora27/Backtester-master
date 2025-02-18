import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HilbertTrendline': 1.0
        })
    )
