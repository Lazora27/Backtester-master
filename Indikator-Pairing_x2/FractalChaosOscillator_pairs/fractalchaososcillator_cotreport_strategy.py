import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'COTReport': 1.0
        })
    )
