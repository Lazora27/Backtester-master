import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
