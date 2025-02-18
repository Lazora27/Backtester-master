import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
