import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und GannAngles
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'GannAngles': 1.0
        })
    )
