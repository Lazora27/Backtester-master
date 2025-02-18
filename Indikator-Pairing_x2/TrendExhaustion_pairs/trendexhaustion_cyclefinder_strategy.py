import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'CycleFinder': 1.0
        })
    )
