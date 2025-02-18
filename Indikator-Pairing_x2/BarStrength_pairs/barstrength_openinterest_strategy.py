import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'OpenInterest': 1.0
        })
    )
