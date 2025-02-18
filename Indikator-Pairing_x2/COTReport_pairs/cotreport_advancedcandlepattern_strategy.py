import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
