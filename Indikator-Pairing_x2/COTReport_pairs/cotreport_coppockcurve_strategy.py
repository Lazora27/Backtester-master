import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'CoppockCurve': 1.0
        })
    )
