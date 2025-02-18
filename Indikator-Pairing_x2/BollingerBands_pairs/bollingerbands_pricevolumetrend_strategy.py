import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
