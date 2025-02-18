import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
