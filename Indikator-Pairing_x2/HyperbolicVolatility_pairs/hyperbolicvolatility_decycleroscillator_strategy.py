import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
