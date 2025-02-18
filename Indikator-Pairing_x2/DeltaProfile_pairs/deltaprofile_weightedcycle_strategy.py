import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'WeightedCycle': 1.0
        })
    )
