import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'WeightedCycle': 1.0
        })
    )
