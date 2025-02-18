import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DeltaProfile': 1.0
        })
    )
