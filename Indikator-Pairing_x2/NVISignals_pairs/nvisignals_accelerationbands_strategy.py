import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AccelerationBands': 1.0
        })
    )
