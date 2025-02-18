import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
