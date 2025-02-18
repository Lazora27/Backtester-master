import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BarStrength
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BarStrength': 1.0
        })
    )
