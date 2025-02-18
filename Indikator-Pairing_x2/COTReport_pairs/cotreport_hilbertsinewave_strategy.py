import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HilbertSinewave': 1.0
        })
    )
