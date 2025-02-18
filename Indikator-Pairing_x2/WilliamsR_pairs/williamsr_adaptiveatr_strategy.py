import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AdaptiveATR': 1.0
        })
    )
