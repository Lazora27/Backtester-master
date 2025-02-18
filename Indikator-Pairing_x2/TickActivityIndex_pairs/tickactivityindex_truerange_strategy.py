import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'TrueRange': 1.0
        })
    )
