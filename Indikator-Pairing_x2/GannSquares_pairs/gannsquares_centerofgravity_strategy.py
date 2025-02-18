import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'CenterOfGravity': 1.0
        })
    )
