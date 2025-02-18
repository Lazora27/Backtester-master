import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
