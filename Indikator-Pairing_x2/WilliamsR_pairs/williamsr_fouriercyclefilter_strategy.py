import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
