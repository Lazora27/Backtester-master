import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'VWAPBands': 1.0
        })
    )
