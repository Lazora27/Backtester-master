import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
