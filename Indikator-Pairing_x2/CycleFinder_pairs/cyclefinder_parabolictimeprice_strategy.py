import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
