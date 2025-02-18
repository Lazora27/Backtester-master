import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'CenterOfGravity': 1.0
        })
    )
