import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
