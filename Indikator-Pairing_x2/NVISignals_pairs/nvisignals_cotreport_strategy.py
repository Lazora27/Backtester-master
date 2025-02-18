import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und COTReport
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'COTReport': 1.0
        })
    )
