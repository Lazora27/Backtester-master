import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'IchimokuCloud': 1.0
        })
    )
