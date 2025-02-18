import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'WeeklyCycle': 1.0
        })
    )
