import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'WeeklyCycle': 1.0
        })
    )
