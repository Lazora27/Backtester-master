import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
