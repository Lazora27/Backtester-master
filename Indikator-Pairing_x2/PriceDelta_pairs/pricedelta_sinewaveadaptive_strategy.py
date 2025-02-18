import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
