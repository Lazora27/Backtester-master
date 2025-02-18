import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und COTReport
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'COTReport': 1.0
        })
    )
