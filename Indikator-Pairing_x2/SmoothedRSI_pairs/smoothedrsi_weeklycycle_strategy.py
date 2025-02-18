import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'WeeklyCycle': 1.0
        })
    )
