import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'VortexIndicator': 1.0
        })
    )
