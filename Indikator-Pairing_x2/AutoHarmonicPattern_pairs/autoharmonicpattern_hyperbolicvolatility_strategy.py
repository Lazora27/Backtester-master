import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
