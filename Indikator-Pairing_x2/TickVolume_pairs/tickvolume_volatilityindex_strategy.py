import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VolatilityIndex': 1.0
        })
    )
