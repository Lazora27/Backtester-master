import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'EaseOfMovement': 1.0
        })
    )
