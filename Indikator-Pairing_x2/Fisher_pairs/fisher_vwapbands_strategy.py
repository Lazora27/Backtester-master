import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VWAPBands
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VWAPBands': 1.0
        })
    )
