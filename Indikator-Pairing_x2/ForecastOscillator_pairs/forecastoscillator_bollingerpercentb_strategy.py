import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
