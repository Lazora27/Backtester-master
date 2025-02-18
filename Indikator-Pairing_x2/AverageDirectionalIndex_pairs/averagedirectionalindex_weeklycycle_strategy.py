import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
