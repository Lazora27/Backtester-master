import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
