import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
