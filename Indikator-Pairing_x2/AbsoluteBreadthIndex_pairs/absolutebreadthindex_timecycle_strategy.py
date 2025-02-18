import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AbsoluteBreadthIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AbsoluteBreadthIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AbsoluteBreadthIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
