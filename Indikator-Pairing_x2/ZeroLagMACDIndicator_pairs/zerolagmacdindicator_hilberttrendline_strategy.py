import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
