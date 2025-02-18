import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
