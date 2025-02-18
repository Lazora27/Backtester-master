import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'COTReport': 1.0
        })
    )
