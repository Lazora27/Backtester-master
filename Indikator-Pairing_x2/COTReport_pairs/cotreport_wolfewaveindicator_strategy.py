import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
