import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VWAPBands
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VWAPBands': 1.0
        })
    )
