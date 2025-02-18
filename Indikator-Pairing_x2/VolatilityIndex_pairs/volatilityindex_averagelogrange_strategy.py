import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
