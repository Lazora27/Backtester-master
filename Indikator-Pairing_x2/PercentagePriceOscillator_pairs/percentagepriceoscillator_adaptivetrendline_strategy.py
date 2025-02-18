import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
