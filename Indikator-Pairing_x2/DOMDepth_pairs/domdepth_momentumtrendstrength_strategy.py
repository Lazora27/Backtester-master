import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
