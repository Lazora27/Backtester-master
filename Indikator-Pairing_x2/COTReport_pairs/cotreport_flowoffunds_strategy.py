import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'FlowOfFunds': 1.0
        })
    )
