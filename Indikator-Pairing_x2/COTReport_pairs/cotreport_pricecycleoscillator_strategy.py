import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
