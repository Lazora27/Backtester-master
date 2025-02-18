import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'EaseOfMovement': 1.0
        })
    )
