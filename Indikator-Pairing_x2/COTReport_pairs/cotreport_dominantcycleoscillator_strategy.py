import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
