import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'WilliamsR': 1.0
        })
    )
