import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AbsoluteBreadthIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AbsoluteBreadthIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AbsoluteBreadthIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
