import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
