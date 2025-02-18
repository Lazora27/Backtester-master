import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ParabolicSAR': 1.0
        })
    )
