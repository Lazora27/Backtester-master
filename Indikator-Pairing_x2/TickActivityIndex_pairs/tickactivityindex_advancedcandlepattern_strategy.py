import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
