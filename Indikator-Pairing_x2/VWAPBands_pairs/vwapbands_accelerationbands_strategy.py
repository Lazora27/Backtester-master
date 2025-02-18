import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'AccelerationBands': 1.0
        })
    )
