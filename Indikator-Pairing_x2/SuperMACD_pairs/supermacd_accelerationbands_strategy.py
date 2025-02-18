import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AccelerationBands': 1.0
        })
    )
