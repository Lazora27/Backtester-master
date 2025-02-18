import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'EhlersDecycler': 1.0
        })
    )
