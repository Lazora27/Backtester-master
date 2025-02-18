import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VortexIndicator': 1.0
        })
    )
