import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
