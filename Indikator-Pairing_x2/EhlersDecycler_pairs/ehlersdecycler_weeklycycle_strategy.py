import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'WeeklyCycle': 1.0
        })
    )
