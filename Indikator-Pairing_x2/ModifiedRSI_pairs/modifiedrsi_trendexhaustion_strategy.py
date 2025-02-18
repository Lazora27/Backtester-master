import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TrendExhaustion': 1.0
        })
    )
