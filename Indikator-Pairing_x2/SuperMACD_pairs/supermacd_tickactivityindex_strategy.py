import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TickActivityIndex': 1.0
        })
    )
