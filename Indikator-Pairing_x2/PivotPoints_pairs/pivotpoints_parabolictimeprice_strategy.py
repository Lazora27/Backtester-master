import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
