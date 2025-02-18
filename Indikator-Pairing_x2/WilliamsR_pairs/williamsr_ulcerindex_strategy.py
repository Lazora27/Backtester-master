import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'UlcerIndex': 1.0
        })
    )
