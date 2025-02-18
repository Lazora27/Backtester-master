import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ProjectionBands': 1.0
        })
    )
