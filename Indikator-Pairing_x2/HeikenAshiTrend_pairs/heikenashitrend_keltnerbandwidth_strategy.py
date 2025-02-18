import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
