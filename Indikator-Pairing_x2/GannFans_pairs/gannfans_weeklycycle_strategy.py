import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'WeeklyCycle': 1.0
        })
    )
