import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TimeCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TimeCycle': 1.0
        })
    )
