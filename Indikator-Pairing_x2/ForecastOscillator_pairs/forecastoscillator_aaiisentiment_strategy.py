import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'AAIISentiment': 1.0
        })
    )
