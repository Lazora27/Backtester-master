import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
