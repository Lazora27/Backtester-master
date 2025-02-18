import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und CyberCycle
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'CyberCycle': 1.0
        })
    )
