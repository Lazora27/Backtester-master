import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'SmoothedCycle': 1.0
        })
    )
