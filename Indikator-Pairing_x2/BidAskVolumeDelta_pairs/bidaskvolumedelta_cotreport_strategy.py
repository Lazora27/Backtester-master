import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und COTReport
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'COTReport': 1.0
        })
    )
