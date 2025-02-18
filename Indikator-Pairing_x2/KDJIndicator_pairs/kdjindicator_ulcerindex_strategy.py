import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
