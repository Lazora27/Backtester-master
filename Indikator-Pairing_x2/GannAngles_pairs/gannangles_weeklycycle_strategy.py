import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'WeeklyCycle': 1.0
        })
    )
