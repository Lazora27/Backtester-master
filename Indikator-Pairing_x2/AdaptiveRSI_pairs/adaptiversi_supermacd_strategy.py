import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SuperMACD
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SuperMACD': 1.0
        })
    )
