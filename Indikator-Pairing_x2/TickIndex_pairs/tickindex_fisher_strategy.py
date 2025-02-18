import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'Fisher': 1.0
        })
    )
