import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'COTReport': 1.0
        })
    )
