import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'COTReport': 1.0
        })
    )
