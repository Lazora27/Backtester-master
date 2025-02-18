import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ParabolicSAR': 1.0
        })
    )
