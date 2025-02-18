import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrend_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrend und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrend': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
