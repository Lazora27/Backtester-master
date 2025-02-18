import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DeltaProfile': 1.0
        })
    )
