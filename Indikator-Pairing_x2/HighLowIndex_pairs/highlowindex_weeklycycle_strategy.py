import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
