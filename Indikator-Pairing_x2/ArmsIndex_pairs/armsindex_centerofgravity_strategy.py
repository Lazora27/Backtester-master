import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
