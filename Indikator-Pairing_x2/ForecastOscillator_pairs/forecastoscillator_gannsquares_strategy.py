import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
