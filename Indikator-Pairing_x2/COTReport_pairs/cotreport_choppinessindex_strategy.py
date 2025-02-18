import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
