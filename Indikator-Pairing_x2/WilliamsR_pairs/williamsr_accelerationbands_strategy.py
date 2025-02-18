import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AccelerationBands': 1.0
        })
    )
