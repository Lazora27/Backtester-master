import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'AccelerationBands': 1.0
        })
    )
