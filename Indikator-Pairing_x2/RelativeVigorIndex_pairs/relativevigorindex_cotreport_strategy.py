import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'COTReport': 1.0
        })
    )
