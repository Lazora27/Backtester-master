import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und COTReport
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'COTReport': 1.0
        })
    )
