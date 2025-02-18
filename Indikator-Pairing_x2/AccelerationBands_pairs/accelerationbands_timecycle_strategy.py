import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'TimeCycle': 1.0
        })
    )
