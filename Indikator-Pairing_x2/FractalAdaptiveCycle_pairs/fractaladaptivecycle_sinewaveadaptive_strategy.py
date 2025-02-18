import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalAdaptiveCycle_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalAdaptiveCycle und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FractalAdaptiveCycle': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
