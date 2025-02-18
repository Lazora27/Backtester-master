import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'DonchianChannels': 1.0
        })
    )
