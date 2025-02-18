import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'BradleySiderograph': 1.0
        })
    )
