import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
