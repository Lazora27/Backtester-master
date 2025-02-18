import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'UlcerIndex': 1.0
        })
    )
