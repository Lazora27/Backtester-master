import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
