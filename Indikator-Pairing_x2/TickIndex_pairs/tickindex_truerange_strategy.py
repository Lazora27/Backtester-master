import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TrueRange': 1.0
        })
    )
