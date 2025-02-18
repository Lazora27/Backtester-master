import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AroonIndicator': 1.0
        })
    )
