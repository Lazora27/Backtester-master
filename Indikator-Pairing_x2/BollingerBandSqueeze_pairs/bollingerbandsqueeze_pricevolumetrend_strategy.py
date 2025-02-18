import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
