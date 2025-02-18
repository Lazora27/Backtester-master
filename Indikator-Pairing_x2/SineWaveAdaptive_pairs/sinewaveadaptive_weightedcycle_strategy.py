import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveAdaptive_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveAdaptive und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SineWaveAdaptive': 1.0,
            'WeightedCycle': 1.0
        })
    )
