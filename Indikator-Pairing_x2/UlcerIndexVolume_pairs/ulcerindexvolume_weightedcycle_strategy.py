import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'WeightedCycle': 1.0
        })
    )
