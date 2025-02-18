import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
