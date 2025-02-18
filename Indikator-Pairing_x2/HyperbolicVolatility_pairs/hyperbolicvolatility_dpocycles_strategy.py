import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'DPOCycles': 1.0
        })
    )
