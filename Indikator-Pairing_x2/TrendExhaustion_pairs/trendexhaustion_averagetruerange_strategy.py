import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AverageTrueRange': 1.0
        })
    )
