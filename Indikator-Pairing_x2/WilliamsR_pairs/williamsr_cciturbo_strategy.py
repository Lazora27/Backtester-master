import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und CCITurbo
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'CCITurbo': 1.0
        })
    )
