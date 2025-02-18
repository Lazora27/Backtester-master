import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
