import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ModifiedATR': 1.0
        })
    )
