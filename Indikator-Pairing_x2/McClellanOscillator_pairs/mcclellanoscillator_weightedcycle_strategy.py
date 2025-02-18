import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
