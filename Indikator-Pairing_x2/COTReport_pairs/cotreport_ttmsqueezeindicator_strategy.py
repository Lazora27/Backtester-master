import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TTMSqueezeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TTMSqueezeIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TTMSqueezeIndicator': 1.0
        })
    )
