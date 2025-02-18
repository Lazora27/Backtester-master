import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und MassIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'MassIndex': 1.0
        })
    )
