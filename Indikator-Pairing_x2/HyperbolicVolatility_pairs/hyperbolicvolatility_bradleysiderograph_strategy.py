import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'BradleySiderograph': 1.0
        })
    )
