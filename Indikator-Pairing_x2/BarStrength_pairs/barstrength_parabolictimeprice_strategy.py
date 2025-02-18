import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
