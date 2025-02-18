import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'WeightedCycle': 1.0
        })
    )
