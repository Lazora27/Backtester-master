import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
