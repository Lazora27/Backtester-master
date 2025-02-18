import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'WeeklyCycle': 1.0
        })
    )
