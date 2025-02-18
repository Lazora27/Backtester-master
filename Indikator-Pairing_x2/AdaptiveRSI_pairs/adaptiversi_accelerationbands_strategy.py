import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AccelerationBands': 1.0
        })
    )
