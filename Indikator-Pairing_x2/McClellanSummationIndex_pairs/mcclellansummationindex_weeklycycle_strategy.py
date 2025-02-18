import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
