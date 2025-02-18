import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
