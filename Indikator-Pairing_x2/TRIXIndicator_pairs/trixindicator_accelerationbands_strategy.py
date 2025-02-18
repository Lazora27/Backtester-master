import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
