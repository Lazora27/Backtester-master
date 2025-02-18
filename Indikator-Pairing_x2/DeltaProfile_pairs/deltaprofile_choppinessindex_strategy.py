import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
