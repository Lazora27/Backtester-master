import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AroonIndicator': 1.0
        })
    )
