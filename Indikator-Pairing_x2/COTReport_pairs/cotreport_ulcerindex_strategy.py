import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'UlcerIndex': 1.0
        })
    )
