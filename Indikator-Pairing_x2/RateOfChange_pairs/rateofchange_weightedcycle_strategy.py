import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WeightedCycle': 1.0
        })
    )
