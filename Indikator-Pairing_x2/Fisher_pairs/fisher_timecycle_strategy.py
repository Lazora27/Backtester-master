import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TimeCycle
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TimeCycle': 1.0
        })
    )
