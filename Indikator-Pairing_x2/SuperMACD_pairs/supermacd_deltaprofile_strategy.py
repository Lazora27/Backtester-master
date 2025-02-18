import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DeltaProfile': 1.0
        })
    )
