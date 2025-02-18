import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
