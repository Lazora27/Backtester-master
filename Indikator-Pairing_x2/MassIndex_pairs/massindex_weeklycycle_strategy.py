import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
