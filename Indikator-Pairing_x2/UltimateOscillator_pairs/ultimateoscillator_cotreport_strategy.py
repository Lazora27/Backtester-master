import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'COTReport': 1.0
        })
    )
