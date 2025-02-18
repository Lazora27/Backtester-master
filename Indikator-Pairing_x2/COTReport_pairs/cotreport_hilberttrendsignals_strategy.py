import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
