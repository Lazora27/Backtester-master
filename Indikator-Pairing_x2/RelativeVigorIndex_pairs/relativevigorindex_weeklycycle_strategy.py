import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
