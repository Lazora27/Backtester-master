import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SineWaveIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
