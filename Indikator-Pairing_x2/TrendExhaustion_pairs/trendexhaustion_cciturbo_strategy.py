import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'CCITurbo': 1.0
        })
    )
