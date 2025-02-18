import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TrendCycles
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TrendCycles': 1.0
        })
    )
