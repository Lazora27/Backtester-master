import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
