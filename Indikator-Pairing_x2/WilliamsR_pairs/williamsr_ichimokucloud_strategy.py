import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'IchimokuCloud': 1.0
        })
    )
