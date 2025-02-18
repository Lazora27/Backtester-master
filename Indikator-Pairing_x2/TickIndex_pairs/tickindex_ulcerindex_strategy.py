import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
