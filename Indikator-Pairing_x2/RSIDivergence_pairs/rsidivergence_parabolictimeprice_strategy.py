import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
