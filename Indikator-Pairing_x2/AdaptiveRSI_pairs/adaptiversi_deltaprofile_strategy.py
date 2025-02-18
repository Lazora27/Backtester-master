import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'DeltaProfile': 1.0
        })
    )
