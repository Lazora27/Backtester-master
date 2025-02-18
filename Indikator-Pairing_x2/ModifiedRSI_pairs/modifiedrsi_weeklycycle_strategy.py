import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'WeeklyCycle': 1.0
        })
    )
