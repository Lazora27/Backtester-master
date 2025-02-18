import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'TimeCycle': 1.0
        })
    )
