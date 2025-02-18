import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
