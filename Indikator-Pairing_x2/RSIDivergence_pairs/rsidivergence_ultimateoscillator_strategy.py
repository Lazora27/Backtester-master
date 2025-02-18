import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'UltimateOscillator': 1.0
        })
    )
