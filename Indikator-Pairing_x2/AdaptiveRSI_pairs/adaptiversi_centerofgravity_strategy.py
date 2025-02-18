import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CenterOfGravity': 1.0
        })
    )
