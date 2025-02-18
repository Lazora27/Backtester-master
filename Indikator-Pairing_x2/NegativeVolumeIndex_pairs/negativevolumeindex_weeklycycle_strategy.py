import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
