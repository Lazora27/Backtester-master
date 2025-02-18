import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
