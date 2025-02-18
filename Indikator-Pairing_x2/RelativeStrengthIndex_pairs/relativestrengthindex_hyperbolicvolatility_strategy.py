import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
