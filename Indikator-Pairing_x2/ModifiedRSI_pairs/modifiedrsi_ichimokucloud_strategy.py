import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'IchimokuCloud': 1.0
        })
    )
