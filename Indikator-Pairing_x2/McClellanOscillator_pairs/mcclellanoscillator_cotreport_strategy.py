import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'COTReport': 1.0
        })
    )
