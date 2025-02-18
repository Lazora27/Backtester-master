import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
