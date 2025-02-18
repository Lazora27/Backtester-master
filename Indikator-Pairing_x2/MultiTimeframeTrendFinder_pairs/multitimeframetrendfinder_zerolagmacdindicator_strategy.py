import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MultiTimeframeTrendFinder_ZeroLagMACDIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MultiTimeframeTrendFinder und ZeroLagMACDIndicator
    """
    
    params = (
        ('indicators', {
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            },
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            }
        }),
        ('weights', {
            'MultiTimeframeTrendFinder': 1.0,
            'ZeroLagMACDIndicator': 1.0
        })
    )
