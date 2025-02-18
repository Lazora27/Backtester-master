import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'AccelerationBands': 1.0
        })
    )
