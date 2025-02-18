import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
