import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
