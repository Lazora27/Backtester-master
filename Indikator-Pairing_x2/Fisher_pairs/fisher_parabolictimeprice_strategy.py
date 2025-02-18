import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
