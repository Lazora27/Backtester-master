import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
