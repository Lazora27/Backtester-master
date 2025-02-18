import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'IchimokuCloud': 1.0
        })
    )
