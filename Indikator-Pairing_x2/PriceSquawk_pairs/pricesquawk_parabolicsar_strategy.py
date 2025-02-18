import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ParabolicSAR': 1.0
        })
    )
