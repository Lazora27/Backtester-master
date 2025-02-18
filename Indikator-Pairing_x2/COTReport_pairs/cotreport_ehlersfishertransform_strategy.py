import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
