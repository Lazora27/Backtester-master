import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
