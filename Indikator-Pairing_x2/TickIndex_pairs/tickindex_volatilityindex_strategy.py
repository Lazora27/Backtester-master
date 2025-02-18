import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
