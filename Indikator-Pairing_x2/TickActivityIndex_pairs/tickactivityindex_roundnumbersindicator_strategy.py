import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
