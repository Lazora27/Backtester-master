import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und COTReport
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'COTReport': 1.0
        })
    )
