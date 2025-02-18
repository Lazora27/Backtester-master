import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
