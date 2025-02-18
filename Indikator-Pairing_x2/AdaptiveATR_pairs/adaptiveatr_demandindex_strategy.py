import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'DemandIndex': 1.0
        })
    )
