import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und BarStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'BarStrength': 1.0
        })
    )
