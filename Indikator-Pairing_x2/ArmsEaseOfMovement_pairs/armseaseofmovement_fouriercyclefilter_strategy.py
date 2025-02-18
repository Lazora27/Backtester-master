import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsEaseOfMovement_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsEaseOfMovement und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ArmsEaseOfMovement': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
