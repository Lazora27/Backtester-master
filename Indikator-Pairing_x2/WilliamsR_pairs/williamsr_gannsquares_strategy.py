import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und GannSquares
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'GannSquares': 1.0
        })
    )
