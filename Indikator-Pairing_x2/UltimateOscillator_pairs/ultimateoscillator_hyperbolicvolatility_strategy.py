import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
