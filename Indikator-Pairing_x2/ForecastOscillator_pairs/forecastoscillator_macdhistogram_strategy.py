import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MACDHistogram': 1.0
        })
    )
