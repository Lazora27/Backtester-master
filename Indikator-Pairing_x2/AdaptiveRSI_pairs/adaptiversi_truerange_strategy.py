import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TrueRange
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TrueRange': 1.0
        })
    )
