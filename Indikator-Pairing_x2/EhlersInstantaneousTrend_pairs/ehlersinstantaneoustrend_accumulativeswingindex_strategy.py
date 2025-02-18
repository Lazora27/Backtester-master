import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrend_AccumulativeSwingIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrend und AccumulativeSwingIndex
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            },
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrend': 1.0,
            'AccumulativeSwingIndex': 1.0
        })
    )
