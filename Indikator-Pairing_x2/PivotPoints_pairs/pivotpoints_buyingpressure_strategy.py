import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'BuyingPressure': 1.0
        })
    )
