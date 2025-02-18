import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
