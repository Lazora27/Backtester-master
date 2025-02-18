import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TickActivityIndex': 1.0
        })
    )
