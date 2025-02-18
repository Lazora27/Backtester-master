import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'AccelerationBands': 1.0
        })
    )
