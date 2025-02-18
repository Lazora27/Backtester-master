import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
