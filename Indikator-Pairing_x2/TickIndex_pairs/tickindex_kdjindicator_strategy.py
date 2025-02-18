import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'KDJIndicator': 1.0
        })
    )
