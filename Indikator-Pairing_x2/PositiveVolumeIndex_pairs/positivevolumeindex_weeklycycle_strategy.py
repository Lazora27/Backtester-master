import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
