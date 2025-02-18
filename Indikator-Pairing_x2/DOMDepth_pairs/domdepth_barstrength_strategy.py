import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BarStrength
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BarStrength': 1.0
        })
    )
