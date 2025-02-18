import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'VortexIndicator': 1.0
        })
    )
