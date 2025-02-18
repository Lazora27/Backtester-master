import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und COTReport
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'COTReport': 1.0
        })
    )
