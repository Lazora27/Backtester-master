import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'DemandIndex': 1.0
        })
    )
