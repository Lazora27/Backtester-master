import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ModifiedRSI': 1.0
        })
    )
