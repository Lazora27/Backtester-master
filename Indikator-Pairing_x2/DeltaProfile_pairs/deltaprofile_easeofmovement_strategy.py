import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'EaseOfMovement': 1.0
        })
    )
