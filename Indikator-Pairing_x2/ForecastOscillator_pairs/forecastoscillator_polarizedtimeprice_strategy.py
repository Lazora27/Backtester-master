import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
