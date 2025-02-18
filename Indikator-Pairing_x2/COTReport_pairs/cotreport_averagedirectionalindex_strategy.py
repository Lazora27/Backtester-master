import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
