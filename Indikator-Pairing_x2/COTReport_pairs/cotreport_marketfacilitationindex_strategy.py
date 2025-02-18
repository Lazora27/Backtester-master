import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
