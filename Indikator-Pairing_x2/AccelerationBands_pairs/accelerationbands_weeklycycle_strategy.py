import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'WeeklyCycle': 1.0
        })
    )
