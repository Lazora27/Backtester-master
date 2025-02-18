import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
