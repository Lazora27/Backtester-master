import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
