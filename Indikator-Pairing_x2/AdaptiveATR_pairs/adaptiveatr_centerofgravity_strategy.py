import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'CenterOfGravity': 1.0
        })
    )
