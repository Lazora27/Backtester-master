import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AccelerationBands': 1.0
        })
    )
