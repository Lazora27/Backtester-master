import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
