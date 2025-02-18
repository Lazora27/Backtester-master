import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
