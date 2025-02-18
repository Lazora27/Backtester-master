import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AccelerationBands': 1.0
        })
    )
