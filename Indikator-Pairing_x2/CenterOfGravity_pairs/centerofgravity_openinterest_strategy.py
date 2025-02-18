import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und OpenInterest
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'OpenInterest': 1.0
        })
    )
