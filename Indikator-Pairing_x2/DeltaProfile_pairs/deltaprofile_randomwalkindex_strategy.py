import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
