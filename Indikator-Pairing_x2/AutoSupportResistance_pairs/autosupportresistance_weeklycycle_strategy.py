import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WeeklyCycle': 1.0
        })
    )
