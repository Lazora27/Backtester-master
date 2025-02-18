import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'WeeklyCycle': 1.0
        })
    )
