import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
