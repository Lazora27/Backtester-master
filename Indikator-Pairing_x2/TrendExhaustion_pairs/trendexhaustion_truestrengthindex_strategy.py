import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
