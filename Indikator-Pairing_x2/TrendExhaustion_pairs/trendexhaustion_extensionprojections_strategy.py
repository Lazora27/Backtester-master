import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ExtensionProjections': 1.0
        })
    )
