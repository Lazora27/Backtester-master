import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
