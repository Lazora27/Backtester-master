import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'WeeklyCycle': 1.0
        })
    )
