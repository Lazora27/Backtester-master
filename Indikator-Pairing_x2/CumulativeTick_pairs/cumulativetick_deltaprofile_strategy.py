import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DeltaProfile': 1.0
        })
    )
