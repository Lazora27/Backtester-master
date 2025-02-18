import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
