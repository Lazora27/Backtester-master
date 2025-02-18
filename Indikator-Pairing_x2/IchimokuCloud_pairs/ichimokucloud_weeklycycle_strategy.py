import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'WeeklyCycle': 1.0
        })
    )
