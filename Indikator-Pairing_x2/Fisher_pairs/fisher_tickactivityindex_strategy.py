import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TickActivityIndex': 1.0
        })
    )
