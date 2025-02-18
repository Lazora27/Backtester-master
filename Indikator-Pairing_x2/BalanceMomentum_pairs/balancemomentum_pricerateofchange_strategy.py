import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
