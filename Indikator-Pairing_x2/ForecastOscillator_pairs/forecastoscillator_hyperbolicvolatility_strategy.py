import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
