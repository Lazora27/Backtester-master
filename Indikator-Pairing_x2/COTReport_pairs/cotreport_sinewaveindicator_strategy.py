import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
