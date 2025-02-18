import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
