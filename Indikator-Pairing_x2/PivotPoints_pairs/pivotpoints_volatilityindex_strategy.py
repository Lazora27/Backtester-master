import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VolatilityIndex': 1.0
        })
    )
