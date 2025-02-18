import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und COTReport
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'COTReport': 1.0
        })
    )
