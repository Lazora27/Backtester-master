import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und BarStrength
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'BarStrength': 1.0
        })
    )
