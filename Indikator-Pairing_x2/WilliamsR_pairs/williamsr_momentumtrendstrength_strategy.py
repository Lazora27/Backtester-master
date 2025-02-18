import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
