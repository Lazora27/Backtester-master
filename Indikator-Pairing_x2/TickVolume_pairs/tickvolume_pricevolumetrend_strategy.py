import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
