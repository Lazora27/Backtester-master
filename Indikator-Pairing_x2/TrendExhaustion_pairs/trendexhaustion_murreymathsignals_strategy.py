import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
