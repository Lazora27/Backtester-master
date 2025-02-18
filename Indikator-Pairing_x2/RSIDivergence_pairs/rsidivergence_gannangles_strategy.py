import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und GannAngles
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'GannAngles': 1.0
        })
    )
