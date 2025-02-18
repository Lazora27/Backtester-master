import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BarStrength
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BarStrength': 1.0
        })
    )
