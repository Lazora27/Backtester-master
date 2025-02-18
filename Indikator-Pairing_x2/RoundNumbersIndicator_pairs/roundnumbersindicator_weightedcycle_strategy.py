import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
