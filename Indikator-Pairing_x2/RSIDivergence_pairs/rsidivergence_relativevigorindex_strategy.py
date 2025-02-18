import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
