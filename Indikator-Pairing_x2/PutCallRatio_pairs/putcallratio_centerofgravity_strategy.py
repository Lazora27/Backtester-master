import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CenterOfGravity': 1.0
        })
    )
