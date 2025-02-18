import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
