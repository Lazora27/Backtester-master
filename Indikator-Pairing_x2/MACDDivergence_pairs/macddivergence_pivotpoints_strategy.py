import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PivotPoints': 1.0
        })
    )
