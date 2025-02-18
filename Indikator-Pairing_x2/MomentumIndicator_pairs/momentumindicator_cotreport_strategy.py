import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und COTReport
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'COTReport': 1.0
        })
    )
