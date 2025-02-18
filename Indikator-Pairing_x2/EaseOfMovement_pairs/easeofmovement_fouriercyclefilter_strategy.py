import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
