import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TrueRange
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TrueRange': 1.0
        })
    )
