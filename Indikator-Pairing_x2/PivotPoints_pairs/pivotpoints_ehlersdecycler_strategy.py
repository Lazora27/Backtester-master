import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'EhlersDecycler': 1.0
        })
    )
