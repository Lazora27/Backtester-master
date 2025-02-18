import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
