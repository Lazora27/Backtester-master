import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und RateOfChange
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'RateOfChange': 1.0
        })
    )
