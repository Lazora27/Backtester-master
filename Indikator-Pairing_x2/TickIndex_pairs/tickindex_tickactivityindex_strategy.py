import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TickActivityIndex': 1.0
        })
    )
