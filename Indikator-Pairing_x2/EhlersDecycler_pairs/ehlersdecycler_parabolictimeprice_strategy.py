import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
