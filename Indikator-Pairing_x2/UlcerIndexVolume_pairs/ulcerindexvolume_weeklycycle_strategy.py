import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'WeeklyCycle': 1.0
        })
    )
