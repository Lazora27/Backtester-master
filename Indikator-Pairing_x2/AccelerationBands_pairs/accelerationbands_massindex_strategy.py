import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und MassIndex
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'MassIndex': 1.0
        })
    )
