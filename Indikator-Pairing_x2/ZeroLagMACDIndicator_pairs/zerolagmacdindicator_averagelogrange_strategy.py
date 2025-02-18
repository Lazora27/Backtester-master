import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
