import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeCycle_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeCycle und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TimeCycle': 1.0,
            'WeightedCycle': 1.0
        })
    )
