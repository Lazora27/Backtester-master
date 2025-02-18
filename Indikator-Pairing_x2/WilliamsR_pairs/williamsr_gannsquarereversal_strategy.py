import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'GannSquareReversal': 1.0
        })
    )
