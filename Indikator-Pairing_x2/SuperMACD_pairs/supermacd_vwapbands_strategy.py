import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VWAPBands
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VWAPBands': 1.0
        })
    )
