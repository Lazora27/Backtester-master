import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
