import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und COTReport
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'COTReport': 1.0
        })
    )
