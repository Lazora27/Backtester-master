import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
