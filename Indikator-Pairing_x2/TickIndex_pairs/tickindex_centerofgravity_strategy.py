import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
