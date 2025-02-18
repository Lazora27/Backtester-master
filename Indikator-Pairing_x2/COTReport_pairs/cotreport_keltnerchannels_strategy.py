import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'KeltnerChannels': 1.0
        })
    )
