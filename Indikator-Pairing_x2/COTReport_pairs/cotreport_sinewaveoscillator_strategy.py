import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
