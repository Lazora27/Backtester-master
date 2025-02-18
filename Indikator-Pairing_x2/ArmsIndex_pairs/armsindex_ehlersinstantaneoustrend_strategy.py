import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_EhlersInstantaneousTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und EhlersInstantaneousTrend
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'EhlersInstantaneousTrend': 1.0
        })
    )
