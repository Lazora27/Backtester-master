import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'COTReport': 1.0
        })
    )
