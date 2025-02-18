import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
