import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'AccelerationBands': 1.0
        })
    )
