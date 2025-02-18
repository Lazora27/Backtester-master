import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und COTReport
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'COTReport': 1.0
        })
    )
