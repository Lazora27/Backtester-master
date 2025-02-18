import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
