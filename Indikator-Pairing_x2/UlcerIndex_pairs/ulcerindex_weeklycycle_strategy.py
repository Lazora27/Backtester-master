import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
