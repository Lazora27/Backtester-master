import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
