import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
