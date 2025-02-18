import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DeltaProfile': 1.0
        })
    )
