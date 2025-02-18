import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DeltaProfile': 1.0
        })
    )
