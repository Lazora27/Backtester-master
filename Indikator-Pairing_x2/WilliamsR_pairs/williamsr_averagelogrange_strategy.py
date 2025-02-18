import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AverageLogRange': 1.0
        })
    )
