import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
