import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
