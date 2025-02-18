import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
