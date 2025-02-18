import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
