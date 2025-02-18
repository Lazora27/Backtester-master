import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
