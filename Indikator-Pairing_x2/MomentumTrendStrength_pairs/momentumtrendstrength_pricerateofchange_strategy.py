import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
