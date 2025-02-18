import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
