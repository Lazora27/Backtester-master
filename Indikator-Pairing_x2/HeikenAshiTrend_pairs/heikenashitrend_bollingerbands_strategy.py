import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und BollingerBands
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'BollingerBands': 1.0
        })
    )
