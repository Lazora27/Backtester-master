import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TrendCycles
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TrendCycles': 1.0
        })
    )
