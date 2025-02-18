import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ForecastOscillator': 1.0
        })
    )
