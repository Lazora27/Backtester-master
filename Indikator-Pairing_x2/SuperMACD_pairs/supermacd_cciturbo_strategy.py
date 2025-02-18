import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CCITurbo
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CCITurbo': 1.0
        })
    )
