import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und Fisher
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'Fisher': 1.0
        })
    )
