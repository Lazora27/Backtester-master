import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und VWAPBands
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'VWAPBands': 1.0
        })
    )
