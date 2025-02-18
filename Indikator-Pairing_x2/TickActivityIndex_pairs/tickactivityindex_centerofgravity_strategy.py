import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
